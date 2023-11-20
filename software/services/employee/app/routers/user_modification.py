from fastapi import APIRouter, HTTPException
from models import user

router = APIRouter()

@router.put("/{user_id}")
def update_user(modificated_user_data : user):
    # TODO: Aktualizacja danych użytkownika w DB
    return {"message": f"User updated successfully"}