"""
Question: 1: 1.	Create a FastAPI app with a GET / route that returns {"message": "Hello, Artificizen"}.

"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    Retrieve specific items belonging to a system user.
    
    - **user_id**: The unique integer ID of the item owner.
    - **q**: Optional search query filter string.
    """
    return {"message": "As'Salaam O Alaikum Artificizen", "status": "success"}