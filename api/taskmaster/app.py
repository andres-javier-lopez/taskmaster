import logging
import sys

from fastapi import FastAPI

from . import __version__


logging.basicConfig(stream=sys.stdout, level=logging.INFO)

app = FastAPI(title="Taskmaster", version=__version__)


@app.get("/")
async def root():
    return f"Taskmaster {__version__}"


@app.get("/ping")
async def ping():
    return "pong"
