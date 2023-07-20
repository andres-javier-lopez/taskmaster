from typing import Any
from uuid import UUID

from taskmaster.core.storage import BaseAdapter
from taskmaster.domain.tasks.entities import Task
from taskmaster.storage.managers.tasks import TasksFilter


class TasksMemoryAdapter(BaseAdapter):
    def __init__(self):
        self.tasks: dict[UUID, Task] = {}

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, ex_tb):
        pass

    async def list(self, filter: dict[TasksFilter, Any] = None) -> list[Task]:
        return list(self.tasks.values())

    async def get(self, uuid: UUID) -> Task | None:
        return self.tasks.get(uuid)

    async def save(self, task: Task):
        self.tasks[task.uuid] = task

    async def delete(self, uuid: UUID):
        del self.tasks[uuid]
