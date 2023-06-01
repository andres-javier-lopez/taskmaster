import logging
import sys

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from . import __version__

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

app = FastAPI(title="Taskmaster", version=__version__)


@app.get("/", response_class=PlainTextResponse)
async def root():
    return f"Taskmaster {__version__}"


@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return "pong"
