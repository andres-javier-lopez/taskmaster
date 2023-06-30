import pytest

from taskmaster.domain.tasks.entities import Task


@pytest.fixture
def task_factory():
    def _task_factory(n=1, **kwargs):
        if n == 1:
            return Task(title="test", **kwargs)
        else:
            return [Task(title=f"test {i}", **kwargs) for i in range(n)]

    return _task_factory
