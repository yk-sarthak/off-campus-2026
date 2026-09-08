from fastapi import FastAPI
from pydantic import BaseModel

tasks=[]

app=FastAPI()

class Task(BaseModel):
    id:int
    task:str
    completion:bool = False

@app.get("/tasks")
def read_tasks():
    return tasks

@app.post("/tasks")
def post_task(task:Task):
    tasks.append(task)
    return task

@app.get("/tasks/{id}")
def get_task(id:int):
    for task in tasks:
        if task.id==id:
            return task
    return {"error":" Task not found"}


@app.put("/tasks/{id}")
def update_task(id:int, updated_task:Task):
    for index,task in enumerate(tasks):
        if task.id==id:
            tasks[index]=updated_task
            return updated_task
    return {"error": "Task not found"}

@app.delete("/tasks/{id}")
def delete_task(id:int):
    for index, task in enumerate(tasks):
        if task.id==id:
            deleted_task=tasks.pop(index)
            return deleted_task
    return {"error": "Task not found"}