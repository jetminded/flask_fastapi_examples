from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse


# baseline

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID must be positive")
    return {"item_id": item_id}


# custom exception

class ItemNotFoundException(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id


@app.exception_handler(ItemNotFoundException) # заметим, что тут можем подставить Exception просто и тогда он будет ловить все ошибки ваши
async def item_not_found_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Item not found",
            "item_id": exc.item_id
        }
    )

fake_db = {"1": "Apple", "2": "Banana"}

@app.get("/products/{item_id}")
async def get_product(item_id: str):
    if item_id not in fake_db:
        raise ItemNotFoundException(item_id=item_id)
    return {"item": fake_db[item_id]}