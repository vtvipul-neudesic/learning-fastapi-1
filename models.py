
# for creating a base class
from sqlalchemy.ext.declarative import declarative_base

# for creating columns and declaring attribute types
from sqlalchemy import String, Integer, Float, Boolean, Column, Text

# creating base class
Base = declarative_base()

# creating item model
class Item(Base):
    __tablename__="item"
    id=Column(Integer, primary_key=True)
    name=Column(String(255), nullable=False)
    price=Column(Float, nullable=False)
    description=Column(Text, nullable=True)
    offer=Column(Boolean, default=False)