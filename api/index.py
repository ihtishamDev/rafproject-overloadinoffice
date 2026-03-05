from fastapi import FastAPI, APIRouter , HTTPException
from typing import List
from api.schema import TaskCreate 
app = FastAPI()


TASKS: List = []
NEXT_ID = 1

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI on Vercel 🚀"}

@app.post("/add")
def create_task(task: TaskCreate):
    global NEXT_ID
    try:
        new_task = ""
        TASKS.append(new_task)
        NEXT_ID += 1
        return new_task
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
    

    try:
        for i, t in enumerate(TASKS):
            if t.id == task_id:
                TASKS.pop(i)
                return {"deleted": True, "task_id": task_id}
        raise HTTPException(status_code=404, detail="Task not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))