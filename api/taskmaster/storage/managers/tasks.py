from enum import Enum
from typing import Any
from uuid import UUID

from taskmaster.core.storage import BaseStorage
from taskmaster.domain.tasks.entities import Task


class TasksFilter(Enum):
    pass


class TasksStorage(BaseStorage):
    Filter = TasksFilter

    async def list(self, filter: dict[Filter, Any]) -> list[Task]:
        return await self.adapter.list(filter)

    async def get(self, uuid: UUID) -> Task | None:
        return await self.adapter.get(uuid)

    async def save(self, task: Task):
        await self.adapter.save(task)

    async def delete(self, uuid: UUID):
        await self.adapter.delete(uuid)
