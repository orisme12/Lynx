import re
from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas import types
from app.schemas import models
from app.deps import create_access_token, get_db
from app.bcrypt import get_password_hash, verify_password
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/login")
async def login(user_credentials: types.UserLogin, db: Session = Depends(get_db)):
    user = user_credentials.model_dump()

    if user["email"] == "" or user["password"] == "":
        return {
            "message": "Dear user, credentials empty.",
            status: status.HTTP_204_NO_CONTENT,
        }

    db_user = db.query(models.User).filter(models.User.email == user["email"]).first()

    if db_user and verify_password(user["password"], db_user.password):
        access_token = create_access_token(data={"sub": user["email"]})
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "message": "User logger successfuly 🐶",
            "db": [],
            "status": status.HTTP_200_OK,
        }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Credentials invalid"
    )


@router.post("/register")
async def register(user_credentials: types.UserCreate, db: Session = Depends(get_db)):
    user = user_credentials.model_dump()
    user["password"] = get_password_hash(user.pop("password")).decode()

    print(user["password"])
    user_exists = (
        db.query(models.User).filter(models.User.email == user["email"]).first()
    )

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    if user["role"] not in ["admin", "user"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="the selected role is incorrect",
        )

    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")

    if not pattern.match(user["email"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="this email is not valid",
        )
    
    if not user["name"] or len(user["name"]) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="the name is not valid",
        )

    db_user = models.User(
        name=user["name"],
        email=user["email"],
        password=user["password"],
        phone=user["phone"],
        role=user["role"],
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "message": "User create successfuly 🐶",
        "db": [],
        "status": status.HTTP_200_OK,
    }
