import pytest
from redis.asyncio import Redis

from taskmaster.domain.tasks.entities import Task
from taskmaster.settings import REDIS_URL
from taskmaster.storage.adapters.tasks.psql import TasksPsqlAdapter
from taskmaster.storage.adapters.tasks.redis import TasksRedisAdapter


@pytest.fixture
def task_factory():
    def _task_factory(n=1, **kwargs):
        if n == 1:
            return Task(title="test", **kwargs)
        else:
            return [Task(title=f"test {i}", **kwargs) for i in range(n)]

    return _task_factory


@pytest.fixture
async def redis_adapter():
    redis = Redis(host=REDIS_URL)
    await redis.flushall()
    yield TasksRedisAdapter(redis)
    await redis.flushall()
    await redis.close()


@pytest.fixture
async def psql_adapter(sessionmaker):
    async with sessionmaker() as session:
        yield TasksPsqlAdapter(session)
