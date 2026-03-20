from datetime import datetime, timezone
import pytest
from pydantic import ValidationError
from models import User, Task

def test_user_creation():
    user = User(id="user_1", email="test@test.com", name="Test User")
    assert user.email == "test@test.com"
    assert user.name == "Test User"
    assert user.createdAt is not None

def test_task_creation():
    task = Task(title="Test Task", user_id="user_1", description="A test description")
    assert task.title == "Test Task"
    assert task.completed is False
    assert task.created_at is not None

def test_task_missing_title():
    with pytest.raises(ValidationError):
        Task.model_validate({"user_id": "user_1"})

def test_task_update_completion():
    task = Task(title="Test", user_id="user_1")
    task.completed = True
    assert task.completed is True
