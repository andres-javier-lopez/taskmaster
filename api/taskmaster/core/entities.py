import dataclasses
import json
from uuid import UUID, uuid4

from taskmaster.core.encoder import CustomEncoder


@dataclasses.dataclass
class Entity:
    # To avoid conflicts with inherited dataclasses use kw_only=True
    uuid: UUID = dataclasses.field(default_factory=uuid4, kw_only=True)

    def __post_init__(self):
        for field in dataclasses.fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                new_value = field.type(value)
                setattr(self, field.name, new_value)

    def to_json(self):
        return json.dumps(dataclasses.asdict(self), cls=CustomEncoder)
