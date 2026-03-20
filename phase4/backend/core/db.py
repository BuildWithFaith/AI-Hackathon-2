import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()
# Get the database URL from the environment, defaulting to sqlite
database_url = os.getenv("DATABASE_URL") or os.getenv("CONNECTION_STRING") or "sqlite:///:memory:"

# Create the SQLAlchemy engine
engine = create_engine(database_url, echo=False)

def get_engine():
    """Returns the database engine."""
    # When testing, environment variable might dynamically change; return a new engine if dynamically required
    # But for a simple test we can just return the initialized one.
    test_db_url = os.getenv("DATABASE_URL") or os.getenv("CONNECTION_STRING") or "sqlite:///:memory:"
    if test_db_url != str(engine.url):
        return create_engine(test_db_url, echo=False)
    return engine

def create_db_and_tables():
    """Create the tables in the database."""
    SQLModel.metadata.create_all(get_engine())

def get_session():
    """Yields a database session."""
    with Session(get_engine()) as session:
        yield session
