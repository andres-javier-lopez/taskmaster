import dataclasses
from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from taskmaster.core.entities import Entity
from taskmaster.core.sqlalchemy import get_connection
from taskmaster.core.storage import BaseAdapter


class BaseSQLAlchemyAdapter(BaseAdapter):
    def __init__(self):
        self.conn = None

    async def __aenter__(self):
        self.conn = await get_connection().__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs):
        old_conn = self.conn
        self.conn = None
        await old_conn.__aexit__(*args, **kwargs)


class BaseModel(AsyncAttrs, DeclarativeBase):
    ModelEntity = None

    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    index: Mapped[Optional[int]] = mapped_column(default=None)

    def to_entity(self) -> Entity:
        fields = dataclasses.fields(self.ModelEntity)
        dict_fields = {field.name: getattr(self, field.name) for field in fields}
        return self.ModelEntity(**dict_fields)

    @classmethod
    def from_entity(cls, entity: Entity):
        return cls(**dataclasses.asdict(entity))
