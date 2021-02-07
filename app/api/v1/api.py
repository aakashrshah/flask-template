from fastapi import APIRouter
from app.api.v1.endpoints import hello, async_hello

api_v1_router = APIRouter()

api_v1_router.include_router(hello.router, tags=["hello"])
api_v1_router.include_router(
    async_hello.router, prefix="/async_hello", tags=["async"])
