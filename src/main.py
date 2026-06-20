from fastapi import FastAPI
from pydantic import BaseModel
from src.core.router import router

app = FastAPI()

app.include_router(router)

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None




# @app.get("/")
# def root():
#     return {"message": "Hello World"}
#
# @app.get("/items/{item_id}")
# def read_item(item_id):
#     return {"item_id": item_id}
#
# @app.post("/items/")
# def create_item(item: Item):
#     return item