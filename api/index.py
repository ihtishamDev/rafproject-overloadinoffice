from fastapi import FastAPI, APIRouter , HTTPException
from typing import List
from api.schema import TaskCreate , TaskResponse
app = FastAPI()

TASKS: List[TaskResponse] = []
NEXT_ID = 1
# router = APIRouter(prefix="/Raf", tags=["Raf"])
@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI on Vercel 🚀"}

@app.post("/add", response_model=TaskResponse)
def create_task(task: TaskCreate):
    global NEXT_ID
    try:
        new_task = TaskResponse(id=NEXT_ID, **task.model_dump())
        TASKS.append(new_task)
        NEXT_ID += 1
        return new_task
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
    

@app.get("/all", response_model=List[TaskResponse])
def get_all_tasks():
    try:
        return TASKS
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

@app.delete("/delete/{task_id}")
def delete_task(task_id: int):
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