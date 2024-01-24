from app.routers.v1 import users, products
from fastapi import APIRouter


router_api = APIRouter()

router_api.include_router(users.router, prefix="/auth", tags=["Authentication"])
router_api.include_router(products.router, prefix='/products', tags=['Products Commerce'])
