import time
from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from fastapi.responses import JSONResponse

app = FastAPI(title="Week 02 Day 05")


def send_welcome_email(user_id: int):
   
    print(f" Starting background process: Sending email to User {user_id}...")
    time.sleep(3)
    print(f" Welcome email successfully SENT to User {user_id}!")


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id > 100:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}



@app.post("/users")
def create_user(user_id: int, background_tasks: BackgroundTasks):
   
    background_tasks.add_task(send_welcome_email, user_id)
    
    return {
        "success": True,
        "message": f"User {user_id} created successfully! Welcome email is being processed.",
        "user_id": user_id
    }