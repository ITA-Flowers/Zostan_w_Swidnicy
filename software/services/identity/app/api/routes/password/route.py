from fastapi import APIRouter, HTTPException, status, Body

from api.models import PasswordResetRequestModel, PasswordChangeRequestModel

router = APIRouter(
    tags=["Password"],
    prefix="/api/identity/password",
)

@router.post(path='/reset',
             description="Resetowanie hasła")
def user_login(data : PasswordResetRequestModel = Body(...)):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Password reset operation not implemented yet!"
    )
    
    
@router.post(path='/change',
             description="Zmiana hasła")
def user_login(data : PasswordChangeRequestModel = Body(...)):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Password change operation not implemented yet!"
    )
