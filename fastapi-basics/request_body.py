from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    Name:str
    price:int
    tax:int | None=None
    description:str | None=None

app=FastAPI()

@app.post("/item/")
def info(item:Item):
    return item