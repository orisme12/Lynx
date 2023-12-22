# File principle

from fastapi import FastAPI
from app.routers.api import router_api
from app.env import API_V1

app = FastAPI()

app.include_router(router_api, prefix=API_V1)
