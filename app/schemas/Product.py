from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.conn import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    image = Column(String)
    is_offer = Column(Boolean)
    offer_price = Column(Integer)
    punctuation = Column(Integer)
    quantity = Column(Integer)
    description = Column(String, index=True)
    brand = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category")
