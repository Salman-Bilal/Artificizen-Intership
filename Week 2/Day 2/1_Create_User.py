"""
Question: 1: 1.	Define a UserCreate model with name: str, email: str, age: int. Create a POST /users route that accepts it and returns it back.
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class UserSchema(BaseModel):
    name: str
    email: str
    age: int


@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):

    return{
        "message": "User is created successfully",
        "User_Name": user.name,
        "Email": user.email,
        "Age": user.age
    }
