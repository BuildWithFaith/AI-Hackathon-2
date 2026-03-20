from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
import pytest
from main import app
from core.db import get_session
from core.auth import get_current_user_id
import jwt

# Setup an in-memory SQLite DB for testing APIs
engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)

def get_session_override():
    with Session(engine) as session:
        yield session

def get_current_user_id_override():
    return "test_user"

app.dependency_overrides[get_session] = get_session_override
app.dependency_overrides[get_current_user_id] = get_current_user_id_override

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_teardown():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)

def test_create_task():
    response = client.post("/api/tasks", json={"title": "Buy groceries", "description": "Milk and eggs"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Buy groceries"
    assert data["user_id"] == "test_user"
    assert data["completed"] is False
    assert "id" in data

def test_get_tasks():
    # Setup some tasks directly or using post
    client.post("/api/tasks", json={"title": "Task 1"})
    client.post("/api/tasks", json={"title": "Task 2"})
    
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_tasks_status_filter():
    res1 = client.post("/api/tasks", json={"title": "Pending Task"})
    res2 = client.post("/api/tasks", json={"title": "Done Task"})
    task2_id = res2.json()["id"]
    client.patch(f"/api/tasks/{task2_id}/complete")
    
    # Filter pending
    res_pending = client.get("/api/tasks?status=pending")
    assert len(res_pending.json()) == 1
    assert res_pending.json()[0]["title"] == "Pending Task"
    
    # Filter completed
    res_completed = client.get("/api/tasks?status=completed")
    assert len(res_completed.json()) == 1
    assert res_completed.json()[0]["title"] == "Done Task"

def test_update_task():
    create_res = client.post("/api/tasks", json={"title": "Old Title"})
    task_id = create_res.json()["id"]
    
    update_res = client.put(f"/api/tasks/{task_id}", json={"title": "New Title", "description": "Updated"})
    assert update_res.status_code == 200
    assert update_res.json()["title"] == "New Title"

def test_delete_task():
    create_res = client.post("/api/tasks", json={"title": "To Delete"})
    task_id = create_res.json()["id"]
    
    delete_res = client.delete(f"/api/tasks/{task_id}")
    assert delete_res.status_code == 200
    
    get_res = client.get("/api/tasks")
    assert len(get_res.json()) == 0

def test_task_isolation():
    # Tasks created are for test_user. Try fetching them when user_id is changed.
    client.post("/api/tasks", json={"title": "Isolated Task"})
    
    app.dependency_overrides[get_current_user_id] = lambda: "other_user"
    res = client.get("/api/tasks")
    assert res.status_code == 200
    assert len(res.json()) == 0
    
    # Restore
    app.dependency_overrides[get_current_user_id] = get_current_user_id_override
