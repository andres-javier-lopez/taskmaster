#!/usr/bin/env bash

export ALEMBIC_CONFIG=taskmaster/core/sqlalchemy/alembic.ini
poetry run alembic upgrade head
poetry run python -m uvicorn taskmaster.app:app --host 0.0.0.0 --port 8001 --reload --log-level info
