from fastapi import FastAPI
from routers import auth, users

app = FastAPI(
    title= "Router Test App",
    description= "Test Application to verify routers",
    version= "1.0.0"
)

@app.get("/")
def read_root():
    return{
        "message": "Main App is running perfectly! Go to /docs to see routers."
    }

app.include_router(auth.router)
app.include_router(users.router)