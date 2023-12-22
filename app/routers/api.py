from app.routers.v1 import users
from fastapi import APIRouter


router_api = APIRouter()

router_api.include_router(users.router, prefix="/auth", tags=["Authentication"])
