
from models import Base, Item

from database import engine

print("creating database...")

Base.metadata.create_all(engine)