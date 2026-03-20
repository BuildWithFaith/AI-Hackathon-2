from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_invalid_request():
    response = client.post("/api/user_1/chat", json={}) # Missing message
    assert response.status_code == 422
