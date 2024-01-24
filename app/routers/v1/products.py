from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.Product import Product
from app.deps import get_db

router = APIRouter()


@router.get("/get")
async def get_products(db: Session = Depends(get_db)):
    products = await db.query(Product).all()

    return products
