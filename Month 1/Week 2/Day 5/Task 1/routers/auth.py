from fastapi import APIRouter

router = APIRouter(
    prefix= "/auth",
    tags=["Authentication"]
)

@router.post("/register")
def test_register():
    return{
        "success": True,
        "message": "Auth router is working! Post request received.",
        "payload_received": "Success"
    }

@router.post('/token')
def test_token():
    return{
        "access_token": "mock_test_token_123",
        "token_type": "bearer"
    }
