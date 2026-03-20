from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field

def get_utc_now():
    return datetime.now(timezone.utc)

# While Better Auth typically manages the User table on the frontend side,
# SQLModel needs a mapping of it if we use SQL relations, or we can just 
# loosely couple and only define the Task model with user_id. 
# We'll define the User table to match BetterAuth just in case.
class User(SQLModel, table=True):
    __tablename__ = "user"
    
    id: str = Field(primary_key=True)
    name: str
    email: str = Field(unique=True, index=True)
    emailVerified: bool = Field(default=False)
    image: Optional[str] = Field(default=None)
    createdAt: datetime = Field(default_factory=get_utc_now)
    updatedAt: datetime = Field(default_factory=get_utc_now)

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True) # Linked to user table but treated loosely for simplicity
    title: str = Field(max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=get_utc_now)
    updated_at: datetime = Field(default_factory=get_utc_now)
