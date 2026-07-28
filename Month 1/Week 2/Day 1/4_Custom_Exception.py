"""
Question: 4: Raise an HTTPException with status 404 and a custom message when a user ID greater than 100 is requested.

"""

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/users/{user_id}")
def get_users(user_id: int):

    if user_id > 100:

        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"User ID {user_id} is not valid. IDs cannot be greater than 100."
        )
    
    return {"user_id": user_id, "status": "Active"}