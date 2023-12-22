from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    phone: Optional[str] = None


class User(BaseModel):
    email: str
    password: str
