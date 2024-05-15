import dataclasses
import json
from typing import Optional

from taskmaster.core.valueobjects import UUID
from taskmaster.core.encoder import CustomEncoder


@dataclasses.dataclass
class Entity:
    # To avoid conflicts with inherited dataclasses use kw_only=True
    uuid: UUID = UUID()
    index: Optional[int] = dataclasses.field(default=None, kw_only=True)

    def to_json(self):
        return json.dumps(dataclasses.asdict(self), cls=CustomEncoder)
