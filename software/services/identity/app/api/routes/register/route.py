from fastapi import APIRouter, HTTPException, status, Body

from api.models import RegisterRequestModel


router = APIRouter(
    tags=["Register"],
    prefix="/api/identity/register",
)

@router.post(path='/',
             description="Rejestracja nowego użytkownika")
def user_register(data : RegisterRequestModel = Body(...)):
    
    # TODO: DB Driver communication -> checkUserExistance, addUserToDB
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="User register operation not implemented yet!"
    )