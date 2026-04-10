# Ссылка на доку: https://fastapi.tiangolo.com/async/

from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Async FastAPI!"}


@app.get("/sync")
def sync_example():
    import time
    time.sleep(2)  # blocks the server
    return {"message": "Blocking"}

@app.get("/async")
async def async_example():
    await asyncio.sleep(2)  # non-blocking
    return {"message": "Non-blocking"}