from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import models
from app.deps import get_db

router = APIRouter()


@router.get("/get")
async def get_products(db: Session = Depends(get_db)):
    products = await db.query(models.Product).all()

    return products
