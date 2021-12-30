from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: float
    offer: bool
    description: str


app = FastAPI()

@app.get('/')
def index():
    return {"message":"Hello world"}

# adding variables in get requests
@app.get("/greet/{name}")
def greeting(name:str):
    return {"message":f"Hello {name}"}

# adding optional strings in get requests
@app.get("/greet")
def greeting_optional(name:Optional[str]="default user2"):
    return {"message":f"Hello {name}"}

# adding an item through post/put request
@app.post("/item/{id}")
def add_item(id:int, item:Item):
    return {
        "id": item.id,
        "name":item.name,
        "price":item.price,
        "offer":item.offer,
        "description":item.description
    }

