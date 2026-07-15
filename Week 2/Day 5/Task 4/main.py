from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Day 5 - Exception Handler Test App"
    )

@app.exception_handler(HTTPException)
async def custom_http_exception(request: Request, exc: HTTPException):

    user_id = request.path_params.get("user_id")
    
    error_payload = {
        "error": True,
        "detail": exc.detail,
        "status": exc.status_code
    }
    
    if user_id is not None:
        error_payload["user"] = f"User {user_id}"

    return JSONResponse(
        status_code=exc.status_code,
        content=error_payload
    )


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id > 50:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {"user_id": user_id}