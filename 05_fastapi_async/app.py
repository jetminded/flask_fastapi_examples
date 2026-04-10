# Ссылка на доку: https://fastapi.tiangolo.com/async/

from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Async FastAPI!"}


@app.get("/sync")
def sync_example():
    print(f"start: {time.time()}")
    time.sleep(10)  # blocks the server
    print(f"end: {time.time()}")
    return {"message": "Blocking"}

@app.get("/async")
async def async_example():
    print(f"start async: {time.time()}")
    await asyncio.sleep(10)  # non-blocking
    print(f"end async: {time.time()}")
    return {"message": "Non-blocking"}
