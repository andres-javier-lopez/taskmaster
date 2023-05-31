from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Entity:
    uuid: UUID = field(default_factory=uuid4)
