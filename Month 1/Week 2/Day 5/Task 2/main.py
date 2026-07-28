import logging
from fastapi import FastAPI, Request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_logger")

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):

    method = request.method
    path = request.url.path

    response = await call_next(request)

    status_code = response.status_code

    logger.info(f"[HTTP LOG] {method} {path} - Response Status: {status_code}")

    return response


@app.get("/")
def read_root():
    return {"message": "Main App is running perfectly! Go to /docs to see routers."}



    