from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Entity:
    # To avoid conflicts with inherited dataclasses use kw_only=True
    uuid: UUID = field(default_factory=uuid4, kw_only=True)
