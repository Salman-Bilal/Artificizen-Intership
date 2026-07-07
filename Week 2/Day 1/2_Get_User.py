"""
Question: 2: 2.	Add a GET /users/{user_id} route that returns the user ID as an integer. Test what happens when you pass a string.

"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):

    """
    Retrieve the user profile by their unique ID.

    - **user_id**: The integer ID of the user to fetch.
    """

    return {"user_id": user_id}

"""
OUTPUT:

At searching this url: http://127.0.0.1:8000/users/25  

Result: It returns user_id:25 

At searching this url: http://127.0.0.1:8000/users/artificizen

Result: {"detail":[{"type":"int_parsing","loc":["path","user_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"aritificizen"}]}

"""