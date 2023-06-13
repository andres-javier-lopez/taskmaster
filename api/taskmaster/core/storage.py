from abc import ABC, abstractmethod
from uuid import UUID

from taskmaster.core.entities import Entity


class BaseAdapter(ABC):
    @abstractmethod
    async def list(self, **kwargs) -> list[Entity]:
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    async def get(self, uuid: UUID) -> Entity:
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    async def save(self, entity: Entity):
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    async def delete(self, uuid: UUID):
        raise NotImplementedError  # pragma: no cover


class BaseStorage(ABC):
    adapter: BaseAdapter

    def __init__(self, adapter: BaseAdapter):
        self.adapter = adapter
