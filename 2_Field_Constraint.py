"""
Question: 2: 2.	Add a Field() constraint to email requiring it to match a basic email pattern, and age must be between 18 and 120.

"""

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()

class UserSchema(BaseModel):
    name: str
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    age: int = Field(..., ge = 18, le = 120)


@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):

    return{
        "message": "User is created successfully",
        "User_Name": user.name,
        "Email": user.email,
        "Age": user.age
    }
