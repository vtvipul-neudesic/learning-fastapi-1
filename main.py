from fastapi import FastAPI, status, HTTPException
from typing import List
from pydantic import BaseModel
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from database import newsession
import models 


# creating a new db session 
db = newsession()

class Item(BaseModel):
    id: int
    name: str
    price: float
    description: str
    offer: bool

    class Config:
        orm_mode=True

# creating a fast api application
app = FastAPI()


@app.get("/items", response_model=List[Item], status_code=status.HTTP_200_OK)
def get_all_items():
    items = db.query(models.Item).all()
    return items


@app.get("/item/{id}", response_model=Item, status_code=status.HTTP_200_OK)
def get_item(id: int):
    item=db.query(models.Item).filter(models.Item.id == id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no item with id {id} exists in the database!")
    else:
        return item

@app.post("/item/create", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item_from_request: Item):

    if db.query(models.Item).filter(item_from_request.id == models.Item.id).first() is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"item with id  {item_from_request.id} already exists")

    new_item = models.Item(
        id=item_from_request.id,
        price=item_from_request.price,
        name=item_from_request.name,
        description=item_from_request.description,
        offer=item_from_request.offer
    )

    db.add(new_item)
    db.commit()        

    return new_item

@app.put("/item/update/{id}", response_model=Item, status_code=HTTP_200_OK)
def update_item(id: int, item: Item):
    itemToUpdate=db.query(models.Item).filter(models.Item.id == id).first()
    if itemToUpdate is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"item with id {id} not found!")
    else:
        itemToUpdate.name = item.name
        itemToUpdate.price = item.price
        itemToUpdate.description = item.description
        itemToUpdate.offer = item.offer

    db.commit()
    return itemToUpdate


@app.delete("/item/{id}", response_model=Item, status_code=status.HTTP_200_OK)
def delete_item(id: int):
    itemToDelete = db.query(models.Item).filter(models.Item.id == id).first()
    if itemToDelete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id {id} not found!")
    else:
        db.delete(itemToDelete)
        db.commit()
    
    return itemToDelete































# class Item(BaseModel):
#     id: int
#     name: str
#     price: float
#     offer: bool
#     description: str


# app = FastAPI()

# @app.get('/')
# def index():
#     return {"message":"Hello world"}

# # adding variables in get requests
# @app.get("/greet/{name}")
# def greeting(name:str):
#     return {"message":f"Hello {name}"}

# # adding optional strings in get requests
# @app.get("/greet")
# def greeting_optional(name:Optional[str]="default user2"):
#     return {"message":f"Hello {name}"}

# # adding an item through post/put request
# @app.post("/item/{id}")
# def add_item(id:int, item:Item):
#     return {
#         "id": item.id,
#         "name":item.name,
#         "price":item.price,
#         "offer":item.offer,
#         "description":item.description
#     }

