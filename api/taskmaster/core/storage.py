from abc import ABC, abstractmethod
from uuid import UUID

from taskmaster.core.entities import Entity


class BaseAdapter(ABC):
    @abstractmethod
    async def list(self, **kwargs) -> list[Entity]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, uuid: UUID) -> Entity:
        raise NotImplementedError

    @abstractmethod
    async def save(self, entity: Entity):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, uuid: UUID):
        raise NotImplementedError


class BaseStorage(ABC):
    adapter: BaseAdapter

    def __init__(self, adapter: BaseAdapter):
        self.adapter = adapter
