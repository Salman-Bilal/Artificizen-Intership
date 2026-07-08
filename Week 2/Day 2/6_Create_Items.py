"""
Question: 6: Create both ItemCreate and ItemRead schemas for a product (name, price, in_stock). The read schema adds created_at. Use response_model to ensure created_at always appears in responses.

"""
from datetime import datetime
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Create_Item(BaseModel):
    name: str
    price: float
    in_stock: bool

class Read_Item(BaseModel):
    name: str
    price: float
    in_stock: bool
    created_at: datetime


@app.post("/items/", response_model=Read_Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Create_Item):
    
    fake_db_item = {
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock,
        "created_at": datetime.now().strftime("%B %d, %Y - %I:%M %p")
    }
    
    return fake_db_item