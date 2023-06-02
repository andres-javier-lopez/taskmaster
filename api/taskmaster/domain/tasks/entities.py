from dataclasses import dataclass
from datetime import date, time
from enum import Enum
from typing import Optional

from taskmaster.core.entities import Entity


@dataclass
class Task(Entity):
    """Represent a pending task on our list"""

    class Status(str, Enum):
        queued = "queued"
        scheduled = "scheduled"
        finished = "finished"
        dropped = "dropped"
        overdue = "overdue"

    class Mood(Enum):
        very_stressed = -3
        stressed = -2
        uncomfortable = -1
        neutral = 0
        good = 1
        excited = 2
        very_excited = 3

    # required fields
    title: str

    # optional fields
    description: str = ""
    status: Status = Status.queued
    due_date: Optional[date] = None  # final date for this task to be done
    scheduled_date: Optional[date] = None  # scheduled date to work on task
    scheduled_time: Optional[time] = None  # optional time to work on task
    estimated_effort_hours: Optional[float] = None
    must_be_done: bool = True
    task_mood: Mood = Mood.neutral

    @property
    def is_open(self):
        return self.status in [
            self.Status.queued,
            self.Status.scheduled,
            self.Status.overdue,
        ]

    def schedule_for(self, date: date, time: Optional[time] = None):
        if self.status in [self.Status.queued, self.Status.scheduled]:
            self.status = self.Status.scheduled
            self.scheduled_date = date
            self.scheduled_time = time

    def unschedule(self):
        if self.status == self.Status.scheduled:
            self.status = self.Status.queued
            self.scheduled_date = None
            self.scheduled_time = None

    def must_be_finished_before(self, date: date):
        self.due_date = date
        self.must_be_done = True

    def drop_it_after(self, date: date):
        self.due_date = date
        self.must_be_done = False

    def update_status_for_date(self, date: date):
        if self.due_date <= date and self.status != self.Status.finished:
            if self.must_be_done:
                self.status = self.Status.overdue
            else:
                self.status = self.Status.dropped
