import pytest

from taskmaster.domain.tasks.entities import Task
from taskmaster.storage.adapters.tasks.memory import TasksMemoryAdapter
from taskmaster.storage.managers.tasks import TasksStorage


@pytest.fixture
def adapter(request, redis_adapter, psql_adapter):
    if request.param == "memory":
        return TasksMemoryAdapter()
    elif request.param == "redis":
        return redis_adapter
    elif request.param == "psql":
        return psql_adapter


async def test_task_model(task_factory):
    task: Task = task_factory()

    from taskmaster.storage.adapters.tasks.psql.model import TaskModel

    model = TaskModel.from_entity(task)
    assert model
    assert model.uuid == task.uuid

    task_from_model = model.to_entity()
    assert task.uuid == task_from_model.uuid
    assert task == task_from_model


@pytest.mark.parametrize("adapter", ["memory", "redis", "psql"], indirect=True)
async def test_tasks_storage_manager(adapter, task_factory):
    storage = TasksStorage(adapter)
    assert (await storage.list()) == []

    task: Task = task_factory()
    await storage.save(task)

    assert (await storage.list()) == [task]
    assert task == (await storage.get(task.uuid))

    task.title = "modified"
    await storage.save(task)
    modified_task = await storage.get(task.uuid)
    assert modified_task.title == "modified"

    await storage.delete(task.uuid)
    assert (await storage.list()) == []
    assert await storage.get(task.uuid) is None

    tasks: list[Task] = task_factory(n=5)
    for task in tasks:
        await storage.save(task)
    assert (await storage.list()) == tasks


@pytest.mark.parametrize("adapter", ["memory", "redis", "psql"], indirect=True)
async def test_tasks_adapter(adapter, task_factory):
    assert (await adapter.list()) == []

    task: Task = task_factory()
    await adapter.save(task)

    assert (await adapter.list()) == [task]
    assert task == (await adapter.get(task.uuid))

    await adapter.delete(task.uuid)
    assert (await adapter.list()) == []
    assert await adapter.get(task.uuid) is None

    tasks: list[Task] = task_factory(n=5)
    for task in tasks:
        await adapter.save(task)
    assert (await adapter.list()) == tasks
