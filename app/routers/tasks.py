from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Dependency: create and close DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=schemas.Task)
def create_new_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.put("/{task_id}", response_model=schemas.Task)
def update_existing_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated = crud.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}")
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
