import os
from sqlmodel import Session
from core.db import get_engine, get_session

def test_get_engine(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    engine = get_engine()
    assert engine is not None
    assert str(engine.url) == "sqlite:///:memory:"

def test_get_session(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    engine = get_engine()
    
    # Check that get_session yields a Session object
    generator = get_session()
    session = next(generator)
    assert isinstance(session, Session)
