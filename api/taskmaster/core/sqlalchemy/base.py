from abc import abstractmethod
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
    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    index: Mapped[Optional[int]] = mapped_column(default=None)

    @abstractmethod
    def to_entity(self) -> Entity:
        raise NotImplementedError
