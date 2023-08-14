from __future__ import annotations

from datetime import date, time
from typing import Optional

from sqlalchemy.orm import Mapped

from taskmaster.core.sqlalchemy.base import BaseModel
from taskmaster.domain.tasks.entities import Task


class TaskModel(BaseModel):
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
        return Task(
            uuid=self.uuid,
            index=self.index,
            title=self.title,
            description=self.description,
            status=self.status,
            due_date=self.due_date,
            scheduled_date=self.scheduled_date,
            scheduled_time=self.scheduled_time,
            estimated_effort_hours=self.estimated_effort_hours,
            must_be_done=self.must_be_done,
            task_mood=self.task_mood,
        )

    @classmethod
    def from_entity(cls, entity: Task) -> TaskModel:
        return cls(
            uuid=entity.uuid,
            index=entity.index,
            title=entity.title,
            description=entity.description,
            status=entity.status,
            due_date=entity.due_date,
            scheduled_date=entity.scheduled_date,
            scheduled_time=entity.scheduled_time,
            estimated_effort_hours=entity.estimated_effort_hours,
            must_be_done=entity.must_be_done,
            task_mood=entity.task_mood,
        )
