from fastapi import APIRouter, HTTPException, status, Body

from api.models import RefreshTokenRequestModel, VerifyTokenRequestModel


router = APIRouter(
    tags=["Auth"],
    prefix="/api/identity/auth",
)

@router.post(path='/refresh',
             description="Odnawianie tokenu")
def token_refresh(data : RefreshTokenRequestModel = Body(...)):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Token refresh operation not implemented yet!"
    )
    
@router.post(path='/verify',
             description="Weryfikowanie tokenu")
def token_verify(data : VerifyTokenRequestModel = Body(...)):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Token verify operation not implemented yet!"
    )