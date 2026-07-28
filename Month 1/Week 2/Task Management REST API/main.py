from fastapi import FastAPI, Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import auth, tasks

# Initialize Database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management System ")

# Global Exception Handler
@app.exception_handler(StarletteHTTPException)
async def custom_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "detail": exc.detail,
            "status": exc.status_code
        }
    )

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Task Manager is running! Head over to /docs to begin."}