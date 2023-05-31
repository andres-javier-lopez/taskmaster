from uuid import UUID

from taskmaster.core.entities import Entity


def test_entity_auto_uuid():
    entity1 = Entity()
    assert isinstance(entity1.uuid, UUID)

    entity2 = Entity()
    assert entity1.uuid != entity2.uuid
