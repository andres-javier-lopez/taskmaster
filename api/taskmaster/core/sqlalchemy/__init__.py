from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from taskmaster.settings import PSQL_CONNECTION_STRING


@asynccontextmanager
async def get_engine() -> AsyncIterator[AsyncEngine]:
    engine = create_async_engine(PSQL_CONNECTION_STRING)
    yield engine
    await engine.dispose()


@asynccontextmanager
async def get_connection() -> AsyncIterator[AsyncConnection]:
    async with get_engine() as engine:
        async with engine.connect() as conn:
            yield conn


@asynccontextmanager
async def get_session(engine) -> AsyncIterator[AsyncSession]:
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    async with async_session() as session:
        yield session
