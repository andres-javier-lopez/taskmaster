from typing import Any
import uuid


class ValueObject:
    def __init__(self, default: Any = None):
        self._default = default

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self._default

        print("default is ", self._default)
        return getattr(instance, self._name, self._default)

    def __set__(self, instance, value):
        setattr(instance, self._name, self.parse(value))

    def parse(self, value):
        self.validate(value)
        return value

    def validate(self, value):
        pass


class UUID(ValueObject):
    def __init__(self):
        pass

    @property
    def _default(self):
        return uuid.uuid4()

    def parse(self, value):
        return uuid.UUID(str(value))
