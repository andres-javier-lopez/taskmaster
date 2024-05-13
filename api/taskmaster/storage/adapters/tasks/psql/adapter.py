from typing import Any, Optional
from uuid import UUID

from sqlalchemy import select

from taskmaster.core.sqlalchemy.base import BaseSQLAlchemyAdapter
from taskmaster.domain.tasks.entities import Task
from taskmaster.storage.managers.tasks import TasksFilter

from .model import TaskModel


class TasksPsqlAdapter(BaseSQLAlchemyAdapter):
    async def list(self, filter: dict[TasksFilter, Any] = None) -> list[Task]:
        stmt = select(TaskModel)
        results = await self.session.execute(stmt)
        return [model.to_entity() for model in results.scalars()]

    async def _get_model(self, uuid: UUID) -> TaskModel:
        return await self.session.get(TaskModel, uuid)

    async def get(self, uuid: UUID) -> Optional[Task]:
        task_model = await self._get_model(uuid)
        if task_model:
            return task_model.to_entity()
        else:
            return None

    async def save(self, task: Task):
        task_model = await self._get_model(task.uuid)
        if task_model:
            task_model.update_from(task)
        else:
            task_model = TaskModel.from_entity(task)
            self.session.add(task_model)
        await self.session.commit()

    async def delete(self, uuid: UUID):
        task_model = await self._get_model(uuid)
        await self.session.delete(task_model)
