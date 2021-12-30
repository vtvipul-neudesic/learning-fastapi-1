# for creating sql engine
from sqlalchemy import create_engine

# for creating a base class
from sqlalchemy.ext.declarative import declarative_base

# for creating a session
from sqlalchemy.orm import sessionmaker


# creating db engine
db_string = "postgres://postgres:root@localhost:5432/item"
engine = create_engine(db_string)

# creating base class
base = declarative_base()

# session to connect to the db engine created above
newsession = sessionmaker(bind=engine)
