from fastapi import FastAPI, Header, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/items/")
async def read_items(
    user_agent: Optional[str] = Header(None),
    x_token: Optional[str] = Header(None),
    x_request_id: Optional[str] = Header(default="unknown")
    # alias: x_custom: str = Header(..., alias="X-Custom-Header")
):
    # Validate a required custom header
    if x_token != "secret-token":
        raise HTTPException(status_code=400, detail="Invalid or missing X-Token")

    return {
        "message": "Headers processed successfully",
        "user_agent": user_agent,
        "x_token": x_token,
        "x_request_id": x_request_id
    }