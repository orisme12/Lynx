from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import models, types
from app.deps import get_db
from app.deps import get_current_user

router = APIRouter()


@router.get("/get")
async def get_categories(db: Session = Depends(get_db)):
    categories = await db.query(models.Category).all()

    return categories


@router.post("/create", dependencies=[Depends(get_current_user)])
async def create_category(current_user: types.User, db: Session = Depends(get_db)):
    print(current_user)
    return {}
