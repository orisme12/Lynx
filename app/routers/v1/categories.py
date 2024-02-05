from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import models
from app.deps import get_db

router = APIRouter()


@router.get("/get")
async def get_categories(db: Session = Depends(get_db)):
    categories = await db.query(models.Category).all()

    return categories
