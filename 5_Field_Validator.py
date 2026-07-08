"""
Question: 5: 5.	Add a @field_validator to reject any name that contains numbers.

"""

from fastapi import FastAPI, status
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

class UserSchema(BaseModel):
    name: str
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    age: int = Field(..., ge = 18, le = 120)

    @field_validator("name")
    @classmethod
    def name_not_contain_num(cls, value: str)-> str:
        if any(char.isdigit() for char in value):
            raise ValueError("Name cannot contain number")
        return value

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):

    return{
        "message": "User is created successfully",
        "User_Name": user.name,
        "Email": user.email,
        "Age": user.age
    }
