from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from taskmaster.core.entities import Entity


class TaskState(str, Enum):
    queued = "queued"
    scheduled = "scheduled"
    finished = "finished"
    dropped = "dropped"


class Mood(Enum):
    very_stressed = -3
    stressed = -2
    uncomfortable = -1
    neutral = 0
    good = 1
    excited = 2
    very_excited = 3


@dataclass
class Task(Entity):
    """Represent a pending task on our list"""

    # required fields
    title: str

    # optional fields
    description: str = ""
    state: TaskState = TaskState.queued
    due_date: Optional[datetime] = None  # final date for this task to be done
    scheduled_for: Optional[datetime] = None  # scheduled date to work on task
    estimated_effort_hours: Optional[float] = None
    must_be_done: bool = True
    task_mood: Mood = Mood.neutral
