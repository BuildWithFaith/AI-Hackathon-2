import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


def generate_uuid() -> str:
    return str(uuid.uuid4())


def get_utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Task:
    title: str
    id: str = field(default_factory=generate_uuid)
    notes: Optional[str] = None
    completed: bool = False
    created_at: str = field(default_factory=get_utc_now_iso)
    updated_at: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "notes": self.notes,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
