"""
Question: 3: 3.	Add a GET /items route with optional query parameters skip (default 0) and limit (default 10) that return a fake paginated list.

"""

from fastapi import FastAPI

app = FastAPI()

DATABASE = [
    {"item_id": 1, "name": "Laptop", "price": 999},
    {"item_id": 2, "name": "Smartphone", "price": 499},
    {"item_id": 3, "name": "Headphones", "price": 99},
    {"item_id": 4, "name": "Keyboard", "price": 49},
    {"item_id": 5, "name": "Monitor", "price": 199},
    {"item_id": 6, "name": "Mouse", "price": 29},
    {"item_id": 7, "name": "Desk Chair", "price": 149},
    {"item_id": 8, "name": "USB-C Cable", "price": 15},
    {"item_id": 9, "name": "Webcam", "price": 79},
    {"item_id": 10, "name": "Microphone", "price": 129}
]

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):

    paginated_items = DATABASE[skip: skip + limit]
    return{
        "skip_value": skip,
        "limit_value": limit,
        "total_returned": len(paginated_items),
        "items": paginated_items
    }