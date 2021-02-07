from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/async")
async def read_root_async():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/async/items/{item_id}")
async def read_item_async(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
