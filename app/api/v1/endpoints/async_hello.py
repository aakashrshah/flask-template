from typing import Optional
from fastapi import APIRouter


router = APIRouter()


@router.get("/async")
async def read_root_async():
    return {"Hello": "World"}


@router.get("/async/items/{item_id}")
async def read_item_async(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
