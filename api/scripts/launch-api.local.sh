#!/usr/bin/env bash

poetry run python -m uvicorn taskmaster.app:app --host 0.0.0.0 --port 8001 --reload --log-level info
