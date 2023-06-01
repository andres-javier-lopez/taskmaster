from datetime import datetime

from taskmaster.domain.tasks.entities import Task, TaskStatus


def test_new_task_required_fields():
    title = "this is a test"

    task = Task(title=title)
    assert task.title == title
    assert task.description == ""
    assert task.due_date is None


def test_new_task_optional_fields():
    title = "this is a test"
    description = "this is a description"
    due_date = datetime.now()

    task = Task(
        title=title,
        description=description,
        due_date=due_date,
    )
    assert task.title == title
    assert task.description == description
    assert task.due_date == due_date


def test_task_schedule(task_factory):
    task: Task = task_factory()
    assert task.status == TaskStatus.queued
    assert task.scheduled_date is None
    assert task.scheduled_time is None

    now = datetime.now()
    task.schedule_for(date=now.date(), time=now.time())
    assert task.status == TaskStatus.scheduled
    assert task.scheduled_date == now.date()
    assert task.scheduled_time == now.time()

    task.unschedule()
    assert task.status == TaskStatus.queued
    assert task.scheduled_date is None
    assert task.scheduled_time is None


def test_task_overdue(task_factory):
    task: Task = task_factory()

    task.must_be_finished_before(datetime.now())
    assert task.must_be_done is True

    task.update_status_for_date(datetime.now())
    assert task.status == TaskStatus.overdue


def test_task_dropped(task_factory):
    task: Task = task_factory()

    task.drop_it_after(datetime.now())
    assert task.must_be_done is False

    task.update_status_for_date(datetime.now())
    assert task.status == TaskStatus.dropped
    assert not task.is_open
