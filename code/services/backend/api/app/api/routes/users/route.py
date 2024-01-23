from fastapi import APIRouter, HTTPException, status
from uuid import UUID

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)

@router.get(path='/{user_uuid}')
def get_user(user_uuid : UUID):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )