from fastapi import APIRouter
from app.schemas.user import User

router = APIRouter()


@router.post("/login")
async def login():
    return {}


@router.post("/register")
async def register(user_credentials: User):
    return {}
