import dataclasses
from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from taskmaster.core.entities import Entity
from taskmaster.core.storage import BaseAdapter


class BaseSQLAlchemyAdapter(BaseAdapter):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session


class BaseModel(AsyncAttrs, DeclarativeBase):
    ModelEntity = None

    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    index: Mapped[Optional[int]] = mapped_column(default=None)

    def to_entity(self) -> Entity:
        fields = dataclasses.fields(self.ModelEntity)
        dict_fields = {field.name: getattr(self, field.name) for field in fields}
        return self.ModelEntity(**dict_fields)

    def update_from(self, entity: Entity):
        fields = dataclasses.asdict(entity)
        for field, value in fields.items():
            setattr(self, field, value)

    @classmethod
    def from_entity(cls, entity: Entity):
        return cls(**dataclasses.asdict(entity))
