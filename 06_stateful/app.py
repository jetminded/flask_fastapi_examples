from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Чем плохо?
# при рестарте можем потерять данные
# Не безопасно при нескольких работниках => не скейлится

app = FastAPI()
user_counters = {}

class User(BaseModel):
    user_id: str


@app.post("/init")
def initialize_user(user: User):
    if user.user_id in user_counters:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_counters[user.user_id] = 0
    return {"message": f"User {user.user_id} initialized"}


@app.post("/increment")
def increment_counter(user: User):
    if user.user_id not in user_counters:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_counters[user.user_id] += 1
    return {
        "user_id": user.user_id,
        "counter": user_counters[user.user_id]
    }


@app.get("/value/{user_id}")
def get_counter(user_id: str):
    if user_id not in user_counters:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": user_id,
        "counter": user_counters[user_id]
    }


@app.delete("/reset/{user_id}")
def reset_counter(user_id: str):
    if user_id not in user_counters:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_counters[user_id] = 0
    return {"message": f"Counter reset for {user_id}"}