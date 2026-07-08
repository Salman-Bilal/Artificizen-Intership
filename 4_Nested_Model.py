"""
Question: 4: Create a nested model: Address with city and country, and embed it in a UserCreate model.

"""

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()

class UserAddress(BaseModel):
    city: str = Field(..., min_length=2)
    country: str = Field(..., min_length=2)

class UserSchema(BaseModel):
    name: str
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    age: int = Field(..., ge = 18, le = 120)

    address: UserAddress


@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):

    return{
        "message": f"User {user.name} is created successfully",
        "User_City": user.address.city,
        "User_Country": user.address.country
    }
