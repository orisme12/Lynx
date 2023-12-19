from fastapi import APIRouter
from src.routers import auth, products

api_router = APIRouter()

api_router.include_router(auth.router, tags=['Login'])
api_router.include_router(products.router, tags=['Products commerce'])
