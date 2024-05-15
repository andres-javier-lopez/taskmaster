from dataclasses import dataclass

from taskmaster.core.entities import Entity
from taskmaster.core.valueobjects import ValueObject


@dataclass
class MockEntity(Entity):
    value: ValueObject = ValueObject(default=1)


def test_valueobject_assignation():
    object = MockEntity()
    assert object.value == 1

    object = MockEntity(value=2)

    assert object.value == 2

    object.value = 3
    assert object.value == 3

    a = object.value
    assert a == 3
