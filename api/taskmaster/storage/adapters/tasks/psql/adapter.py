from uuid import UUID

from taskmaster.core.entities import Entity
from taskmaster.core.sqlalchemy.adapter import BaseSQLAlchemyAdapter


class TasksPsqlAdapter(BaseSQLAlchemyAdapter):
    async def list(self, **kwargs) -> list[Entity]:
        return await super().list(**kwargs)

    async def get(self, uuid: UUID) -> Entity:
        return await super().get(uuid)

    async def save(self, entity: Entity):
        return await super().save(entity)

    async def delete(self, uuid: UUID):
        return await super().delete(uuid)
