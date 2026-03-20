from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional
from pydantic import BaseModel

from core.db import get_session
from core.auth import get_current_user_id
from models import Task

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

@router.get("", response_model=List[Task])
def get_tasks(
    status: str = Query("all", description="Filter tasks: all, pending, completed"),
    user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    query = select(Task).where(Task.user_id == user_id)
    
    if status == "pending":
        query = query.where(Task.completed == False)
    elif status == "completed":
        query = query.where(Task.completed == True)
        
    tasks = session.exec(query).all()
    return tasks

@router.post("", response_model=Task)
def create_task(
    task_in: TaskCreate,
    user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    task = Task(title=task_in.title, description=task_in.description, user_id=user_id)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.put("/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task_in: TaskUpdate,
    user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    task = session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")
        
    if task_in.title is not None:
        task.title = task_in.title
    if task_in.description is not None:
        task.description = task_in.description
        
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.patch("/{task_id}/complete", response_model=Task)
def complete_task(
    task_id: int,
    user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    task = session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")
        
    task.completed = not task.completed
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    task = session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")
        
    session.delete(task)
    session.commit()
    return {"ok": True}
