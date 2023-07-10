from taskmaster.domain.tasks.entities import Task
from taskmaster.storage.adapters.tasks.memory import TasksMemoryAdapter
from taskmaster.storage.managers.tasks import TasksStorage


async def test_tasks_storage_manager(task_factory):
    adapter = TasksMemoryAdapter()
    storage = TasksStorage(adapter)

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
    adapter = TasksMemoryAdapter()

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