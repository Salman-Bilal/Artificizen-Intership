from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()

users = []

security = HTTPBearer(auto_error=False)

@app.post("/users", status_code=201)
def create_user(user: dict):
    
    for u in users:
        if u["email"] == user["email"]:
            raise HTTPException(
                status_code=409, 
                detail="Email already exists"
                )

    users.append(user)
    return user

@app.get("/profile")
def profile(credentials: HTTPAuthorizationCredentials = Depends(security)):

    if credentials is None:
        raise HTTPException(
            status_code=401, 
            detail="Not authenticated"
            )


    return {"message": "Protected Route"}