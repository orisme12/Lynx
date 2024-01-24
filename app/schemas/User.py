from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db.conn import Base
from pydantic import BaseModel
from typing import Optional


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    role = Column(String, default="user")

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    phone: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str
