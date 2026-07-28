from fastapi import APIRouter, Depends
from db.models import User
from services.auth import get_current_user

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/{room_id}")
def send_chat(room_id: int, current_user: User = Depends(get_current_user)):
    return {"message": f"Chat endpoint placeholder for room {room_id}"}

@router.get("/{room_id}/history")
def get_chat_history(room_id: int, current_user: User = Depends(get_current_user)):
    return {"history": []}