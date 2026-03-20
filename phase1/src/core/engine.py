from typing import List, Optional, Dict
from .models import Task, get_utc_now_iso
from .exceptions import NotFoundError, ValidationError


class InMemoryTodoEngine:
    def __init__(self):
        self._tasks: Dict[str, Task] = {}

    def get_task(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)

    def create_task(self, title: str, notes: Optional[str] = None) -> Task:
        if not title or not title.strip():
            raise ValidationError("Title cannot be empty")
        task = Task(title=title.strip(), notes=notes)
        self._tasks[task.id] = task
        return task

    def list_tasks(self, status: Optional[str] = "pending") -> List[Task]:
        tasks = list(self._tasks.values())
        if status == "completed":
            return [t for t in tasks if t.completed]
        elif status == "pending":
            return [t for t in tasks if not t.completed]
        return tasks

    def complete_task(self, task_id: str) -> Task:
        task = self.get_task(task_id)
        if not task:
            raise NotFoundError(f"Task with id {task_id} not found")
        task.completed = True
        task.updated_at = get_utc_now_iso()
        return task

    def delete_task(self, task_id: str) -> bool:
        if task_id not in self._tasks:
            raise NotFoundError(f"Task with id {task_id} not found")
        del self._tasks[task_id]
        return True

    def update_task(
        self, task_id: str, title: Optional[str] = None, notes: Optional[str] = None
    ) -> Task:
        task = self.get_task(task_id)
        if not task:
            raise NotFoundError(f"Task with id {task_id} not found")
        if title is not None:
            if not title.strip():
                raise ValidationError("Title cannot be empty")
            task.title = title.strip()
        if notes is not None:
            task.notes = notes
        task.updated_at = get_utc_now_iso()
        return task
