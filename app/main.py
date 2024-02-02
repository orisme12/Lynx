from fastapi import FastAPI
from app.routers.api import router_api
from app.env import API_V1
from fastapi.middleware.cors import CORSMiddleware
from app.db.conn import engine
from app.schemas import models


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_api, prefix=API_V1)
