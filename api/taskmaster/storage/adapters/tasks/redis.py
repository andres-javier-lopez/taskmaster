import asyncio
import json
from typing import Any
from uuid import UUID

from redis.asyncio import Redis

from taskmaster.core.storage import BaseAdapter
from taskmaster.domain.tasks.entities import Task
from taskmaster.settings import REDIS_URL
from taskmaster.storage.managers.tasks import TasksFilter


class TasksRedisAdapter(BaseAdapter):
    prefix = "tasks:"

    def __init__(self):
        self.redis = Redis(host=REDIS_URL)

    async def _get_task(self, key) -> Task | None:
        json_data = await self.redis.get(key)
        if json_data is None:
            return None
        data = json.loads(json_data)
        return Task(**data)

    async def _keys(self) -> list:
        return await self.redis.keys(pattern=self.prefix + "*")

    async def _count(self) -> int:
        keys = await self._keys()
        return len(keys)

    async def list(self, filter: dict[TasksFilter, Any] = None) -> list[Task]:
        keys = await self._keys()
        tasks = await asyncio.gather(*[self._get_task(key) for key in keys])

        tasks.sort(key=lambda t: t.index)
        return tasks

    async def get(self, uuid: UUID) -> Task:
        return await self._get_task(self.prefix + str(uuid))

    async def save(self, task: Task):
        index = await self._count()
        task.index = index
        data = task.to_json()
        await self.redis.set(self.prefix + str(task.uuid), data)

    async def delete(self, uuid: UUID):
        await self.redis.delete(self.prefix + str(uuid))
