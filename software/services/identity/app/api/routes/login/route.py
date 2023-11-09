from fastapi import APIRouter, HTTPException, status, Body

from api.models import LoginRequestModel, LogoutRequestModel


router = APIRouter(
    tags=["Login"],
    prefix="/api/identity",
)

@router.post(path='/login/user',
             description="Uwierzytelnienie użytkownika")
def user_login(data : LoginRequestModel = Body(...)):
    # TODO: DB Driver communication -> checkUserExistance
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="User login operation not implemented yet!"
    )


@router.post(path='/login/company',
             description="Uwierzytelnienie przedsiębiorstwa")
def company_login(data : LoginRequestModel = Body(...)):
    # TODO: DB Driver communication -> checkUserExistance
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Company login operation not implemented yet!"
    )


@router.post(path='/logout',
             description="Wylogowanie")
def logout(data : LogoutRequestModel = Body(...)):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Logout operation not implemented yet!"
    )