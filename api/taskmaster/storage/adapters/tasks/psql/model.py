from __future__ import annotations

from datetime import date, time
from typing import Optional

from sqlalchemy.orm import Mapped

from taskmaster.core.sqlalchemy.base import BaseModel
from taskmaster.domain.tasks.entities import Task


class TaskModel(BaseModel):
    ModelEntity = Task
    __tablename__ = "tasks"

    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[Task.Status]
    due_date: Mapped[Optional[date]]
    scheduled_date: Mapped[Optional[date]]
    scheduled_time: Mapped[Optional[time]]
    estimated_effort_hours: Mapped[Optional[float]]
    must_be_done: Mapped[bool]
    task_mood: Mapped[Task.Mood]

    def to_entity(self) -> Task:
        return super().to_entity()
