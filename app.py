from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI(title="Gen-AI Task Board")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    id: str
    title: str
    completed: bool = False
    category: str
    priority: str

class TaskCreate(BaseModel):
    title: str

tasks: List[Task] = []

def analyze_task(title: str):
    t = title.lower()
    if any(w in t for w in ["study", "learn", "read"]):
        return "Learning", "Medium"
    if any(w in t for w in ["code", "build", "deploy"]):
        return "Coding", "High"
    if any(w in t for w in ["gym", "health"]):
        return "Health", "Medium"
    if any(w in t for w in ["meet", "call"]):
        return "Meeting", "High"
    return "General", "Low"

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: TaskCreate):
    category, priority = analyze_task(task.title)
    new_task = Task(
        id=str(uuid4()),
        title=task.title,
        category=category,
        priority=priority
    )
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}")
def toggle_task(task_id: str):
    for t in tasks:
        if t.id == task_id:
            t.completed = not t.completed
            return t
    return {"error": "Not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"message": "Deleted"}

@app.get("/progress")
def progress():
    if not tasks:
        return {"progress": 0}
    done = len([t for t in tasks if t.completed])
    return {"progress": int((done / len(tasks)) * 100)}

@app.get("/ai-summary")
def ai_summary():
    completed = [t for t in tasks if t.completed]
    return {"message": f"You completed {len(completed)} tasks today 🎉"}
