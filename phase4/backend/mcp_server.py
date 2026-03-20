from sqlmodel import Session, select
from core.db import engine
from models import Task
from mcp.server.fastmcp import FastMCP
from typing import Optional, List
import sys

# Create FastMCP instance
mcp = FastMCP("TodoMCP")

@mcp.tool()
def add_task(user_id: str, title: str, description: Optional[str] = None) -> dict:
    """Create a new task"""
    print(f"Executing add_task: user_id={user_id}, title={title}, desc={description}", file=sys.stderr)
    try:
        with Session(engine) as session:
            task = Task(user_id=user_id, title=title, description=description)
            session.add(task)
            session.commit()
            session.refresh(task)
            print(f"Task inserted successfully! ID={task.id}", file=sys.stderr)
            return {"task_id": task.id, "status": "created", "title": task.title}
    except Exception as e:
        print(f"DB EXCEPTION in add_task: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        return {"error": str(e)}

@mcp.tool()
def list_tasks(user_id: str, status: str = "all") -> List[dict]:
    """Retrieve tasks from the list for the user based on status (all, pending, completed)"""
    with Session(engine) as session:
        query = select(Task).where(Task.user_id == user_id)
        if status == "pending":
            query = query.where(Task.completed == False)
        elif status == "completed":
            query = query.where(Task.completed == True)
        tasks = session.exec(query).all()
        return [{"id": t.id, "title": t.title, "completed": t.completed} for t in tasks]

@mcp.tool()
def complete_task(user_id: str, task_id: int) -> dict:
    """Mark a task as complete"""
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task or task.user_id != user_id:
            return {"error": "Task not found"}
        task.completed = True
        session.add(task)
        session.commit()
        session.refresh(task)
        return {"task_id": task.id, "status": "completed", "title": task.title}

@mcp.tool()
def delete_task(user_id: str, task_id: int) -> dict:
    """Remove a task from the list"""
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task or task.user_id != user_id:
            return {"error": "Task not found"}
        title = task.title
        session.delete(task)
        session.commit()
        return {"task_id": task_id, "status": "deleted", "title": title}

@mcp.tool()
def update_task(user_id: str, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> dict:
    """Modify task title or description"""
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task or task.user_id != user_id:
            return {"error": "Task not found"}
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        session.add(task)
        session.commit()
        session.refresh(task)
        return {"task_id": task.id, "status": "updated", "title": task.title}
if __name__ == "__main__":
    mcp.run()
