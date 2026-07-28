from fastapi import APIRouter, Depends
from db.models import User
from services.auth import get_current_user

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/{room_id}")
def upload_file(room_id: int, current_user: User = Depends(get_current_user)):
    return {"message": f"Upload endpoint placeholder for room {room_id}"}