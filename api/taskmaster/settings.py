import os

from dotenv import load_dotenv

load_dotenv()

REDIS_URL = "redis"
PSQL_CONNECTION_STRING = os.getenv("PSQL_CONNECTION_STRING")
