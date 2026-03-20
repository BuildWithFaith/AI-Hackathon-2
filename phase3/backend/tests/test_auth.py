from fastapi import Request, HTTPException
import pytest
from core.auth import get_current_user_id
import jwt

def test_get_current_user_id_valid_token():
    token = jwt.encode({"sub": "user_123"}, "secret", algorithm="HS256")
    
    class MockRequest:
        headers = {"Authorization": f"Bearer {token}"}
    
    user_id = get_current_user_id(request=MockRequest(), secret_key="secret")
    assert user_id == "user_123"

def test_get_current_user_id_missing_token():
    class MockRequest:
        headers = {}
    
    with pytest.raises(HTTPException) as excinfo:
        get_current_user_id(request=MockRequest(), secret_key="secret")
    assert excinfo.value.status_code == 401

def test_get_current_user_id_invalid_token():
    class MockRequest:
        headers = {"Authorization": "Bearer invalid_token"}
    
    with pytest.raises(HTTPException) as excinfo:
        get_current_user_id(request=MockRequest(), secret_key="secret")
    assert excinfo.value.status_code == 401
