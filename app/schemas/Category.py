from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db.conn import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("Product", back_populates="category")
