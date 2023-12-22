from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate
from app.deps import get_password_hash, verify_password, create_access_token
from app.db.connection import users_collection
from app.schemas.user import User

router = APIRouter()


@router.post("/login")
async def login(user_credentials: User):
    hash_user = user_credentials.model_dump()
    if hash_user["email"] == "" or hash_user["password"] == "":
        return {"message": "Dear user, campus empty."}
    storage_user = users_collection.find_one({"email": hash_user["email"]})

    if storage_user is not None:
        verify_password_user = verify_password(
            hash_user["password"], storage_user.get("password")
        )
        if storage_user and verify_password_user:
            access_token = create_access_token(data={"sub": hash_user["email"]})
            return {
                "access_token": access_token,
                "token_type": "bearer",
                "message": "Sing In... Welcome user",
            }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Credentials invalid"
    )


@router.post("/register")
async def register(user_credentials: UserCreate):
    storage_user = users_collection.find_one({"email": user_credentials.email})
    if storage_user:
        return {"message": "Dear user, this email is already in use."}

    if user_credentials.email == "" or user_credentials.password == "":
        return {"message": "Dear user, campus empty."}

    hash_user = user_credentials.model_dump()
    hash_user["password"] = get_password_hash(hash_user.pop("password"))
    user_id = users_collection.insert_one(hash_user).inserted_id

    return {
        "username": user_credentials.name,
        "email": user_credentials.email,
        "_id": str(user_id),
        "message": "User successfuly register",
    }
