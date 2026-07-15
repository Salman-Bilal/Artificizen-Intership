from fastapi import APIRouter

router = APIRouter(
    prefix= "/users",
    tags= ["Users"]
)

@router.get("/me")
def get_me():
    return{
        
        "success": True,
        "message": "Users router is working! GET /users/me request received.",
        "user": {
            "id": 1,
            "username": "test_user@example.com",
            "role": "admin"
        }

    }