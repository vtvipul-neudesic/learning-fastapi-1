# for creating sql engine
from sqlalchemy import create_engine

# for creating a session
from sqlalchemy.orm import sessionmaker


# creating db engine
db_string = "postgresql://postgres:root@localhost:5432/item_db"
engine = create_engine(db_string, echo=True)

# session to connect to the db engine created above
newsession = sessionmaker(bind=engine)