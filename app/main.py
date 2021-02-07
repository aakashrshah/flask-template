from fastapi import FastAPI
from app.api.v1.api import api_v1_router
from app.config import API_V1_STR

app = FastAPI()
# app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")s

app.include_router(api_v1_router, prefix=API_V1_STR)
