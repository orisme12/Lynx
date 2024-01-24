import bcrypt
import os
from jose import jwt, ExpiredSignatureError, JWTError
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from app.db.conn import SessionLocal

JWT_SECRET = os.environ.get("JWT_SECRET") or ""
SECRET_KEY = os.environ.get("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
ALGORITHM = os.environ.get("ALGORITHM")

salt = bcrypt.gensalt()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=JWT_SECRET)


def verify_password(plain_password: str, hashed_password: str):
    enconde_password = plain_password.encode()
    return bcrypt.checkpw(enconde_password, hashed_password)


def get_password_hash(password: str):
    enconde_password = password.encode()
    passowrd_hashed = bcrypt.hashpw(enconde_password, salt)
    return passowrd_hashed


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_enconde = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_enconde.update({"exp": expire})
    token = jwt.encode(to_enconde, SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except ExpiredSignatureError:
        raise credentials_exception
    except JWTError:
        raise credentials_exception


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
