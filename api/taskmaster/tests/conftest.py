import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from taskmaster.core.sqlalchemy.base import BaseModel


@pytest.fixture
def test_client():
    from taskmaster.app import app

    return TestClient(app)


@pytest.fixture
async def test_db_engine():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    return engine


@pytest.fixture
def sessionmaker(test_db_engine):
    return async_sessionmaker(test_db_engine, expire_on_commit=False)
