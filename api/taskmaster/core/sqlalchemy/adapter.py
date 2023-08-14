from taskmaster.core.sqlalchemy import get_connection
from taskmaster.core.storage import BaseAdapter


class BaseSQLAlchemyAdapter(BaseAdapter):
    def __init__(self):
        self.conn = None

    async def __aenter__(self):
        self.conn = await get_connection().__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs):
        old_conn = self.conn
        self.conn = None
        await old_conn.__aexit__(*args, **kwargs)
