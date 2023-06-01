import pytest

from taskmaster.domain.tasks.entities import Task


@pytest.fixture
def task_factory():
    def _task_factory(**kwargs):
        return Task(title="test", **kwargs)

    return _task_factory
