from datetime import datetime

from taskmaster.domain.tasks.entities import Task


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
