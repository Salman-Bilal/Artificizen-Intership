from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["https://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.middleware("http")
async def log_requests(request: Request, call_next):

    method = request.method
    path = request.url.path

    response = await call_next(request)

    status_code = response.status_code
    
    print(
        f"Method: {method} | "
        f"Path: {path} | "
        f"Status Code: {status_code}"
    )

    return response

@app.get("/")
def read_root():
    return{
        "message": "CORS Middleware added Successfully!"
    }





    