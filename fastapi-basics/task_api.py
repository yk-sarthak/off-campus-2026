from fastapi import FastAPI, HTTPException , Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Task as TaskModel

app=FastAPI()

class Task(BaseModel):
    title: str
    done: bool = False

@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    return db.query(TaskModel).all()

@app.post("/tasks")
def post_task(task: Task, db: Session = Depends(get_db)):
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task



@app.get("/tasks/{id}")
def get_task(id:int,db:Session=Depends(get_db)):
    task=db.query(TaskModel).filter(TaskModel.id==id).first()
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    return task
    


@app.put("/tasks/{id}")
def update_task(id:int, updated_task:Task, db:Session=Depends(get_db)):
    task=db.query(TaskModel).filter(TaskModel.id==id).first()
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
            )
    task.title=updated_task.title
    task.done=updated_task.done
    db.commit()
    return task
    

@app.delete("/tasks/{id}")
def delete_task(id:int,db:Session=Depends(get_db)):
    task=db.query(TaskModel).filter(TaskModel.id==id).first()
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    db.delete(task)
    db.commit()
    return {"message":"Task deleted successfully"}