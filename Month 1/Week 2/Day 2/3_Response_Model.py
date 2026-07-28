"""
Question: 3: 3.	Create a UserRead model that adds an id: int field. Use response_model=UserRead on the route so the response always includes an id.

"""

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()

class UserSchema(BaseModel):
    name: str
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    age: int = Field(..., ge = 18, le = 120)

class ReadUser(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/",response_model=ReadUser , status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):

    fake_user_db = {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

    return fake_user_db
