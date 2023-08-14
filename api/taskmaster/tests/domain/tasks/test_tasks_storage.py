import pytest

from taskmaster.domain.tasks.entities import Task
from taskmaster.storage.adapters.tasks.memory import TasksMemoryAdapter
from taskmaster.storage.adapters.tasks.psql import TasksPsqlAdapter
from taskmaster.storage.adapters.tasks.redis import TasksRedisAdapter
from taskmaster.storage.managers.tasks import TasksStorage


async def test_tasks_storage_manager(task_factory):
    adapter = TasksMemoryAdapter()
    async with TasksStorage.context(adapter) as storage:
        assert (await storage.list()) == []

        task: Task = task_factory()
        await storage.save(task)

        assert (await storage.list()) == [task]
        assert task == (await storage.get(task.uuid))

        await storage.delete(task.uuid)
        assert (await storage.list()) == []
        assert await storage.get(task.uuid) is None

        tasks: list[Task] = task_factory(n=5)
        for task in tasks:
            await storage.save(task)
        assert (await storage.list()) == tasks


async def test_tasks_memory_adapter(task_factory):
    async with TasksMemoryAdapter() as adapter:
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


async def test_tasks_redis_adapter(task_factory):
    async with TasksRedisAdapter() as adapter:
        await adapter.redis.flushall()

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

        await adapter.redis.flushall()


async def test_task_model(task_factory):
    task: Task = task_factory()

    from taskmaster.storage.adapters.tasks.psql.model import TaskModel

    model = TaskModel.from_entity(task)
    print(model)
    assert model
    assert model.uuid == task.uuid

    task_from_model = model.to_entity()
    print(task_from_model)
    assert task.uuid == task_from_model.uuid
    assert task == task_from_model


@pytest.mark.xfail
async def test_task_psql_adapter(task_factory):
    async with TasksPsqlAdapter() as adapter:
        assert (await adapter.list()) == []
