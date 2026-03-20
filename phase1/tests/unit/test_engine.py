import pytest
from src.core.engine import InMemoryTodoEngine
from src.core.exceptions import ValidationError


def test_create_task_success():
    engine = InMemoryTodoEngine()
    task = engine.create_task("Buy milk", notes="2% milk")

    assert task.title == "Buy milk"
    assert task.notes == "2% milk"
    assert task.completed is False
    assert task.id is not None
    assert engine.get_task(task.id) == task


def test_create_task_empty_title():
    engine = InMemoryTodoEngine()
    with pytest.raises(ValidationError):
        engine.create_task("   ")


def test_list_tasks():
    engine = InMemoryTodoEngine()
    engine.create_task("Task 1")
    task2 = engine.create_task("Task 2")
    task2.completed = True

    all_tasks = engine.list_tasks("all")
    assert len(all_tasks) == 2

    pending = engine.list_tasks("pending")
    assert len(pending) == 1
    assert pending[0].title == "Task 1"

    completed = engine.list_tasks("completed")
    assert len(completed) == 1
    assert completed[0].title == "Task 2"


def test_complete_task():
    engine = InMemoryTodoEngine()
    task = engine.create_task("Finish project")
    assert task.completed is False

    completed_task = engine.complete_task(task.id)
    assert completed_task.completed is True
    assert engine.get_task(task.id).completed is True


def test_complete_task_not_found():
    engine = InMemoryTodoEngine()
    from src.core.exceptions import NotFoundError

    with pytest.raises(NotFoundError):
        engine.complete_task("invalid-id")


def test_delete_task():
    engine = InMemoryTodoEngine()
    task = engine.create_task("Delete me")
    assert len(engine.list_tasks()) == 1

    deleted = engine.delete_task(task.id)
    assert deleted is True
    assert len(engine.list_tasks()) == 0


def test_delete_task_not_found():
    engine = InMemoryTodoEngine()
    from src.core.exceptions import NotFoundError

    with pytest.raises(NotFoundError):
        engine.delete_task("invalid-id")


def test_update_task():
    engine = InMemoryTodoEngine()
    task = engine.create_task("Old title", "Old notes")

    updated = engine.update_task(task.id, title="New title")
    assert updated.title == "New title"
    assert updated.notes == "Old notes"

    updated = engine.update_task(task.id, notes="New notes")
    assert updated.notes == "New notes"
    assert updated.title == "New title"
