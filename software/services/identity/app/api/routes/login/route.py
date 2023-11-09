from fastapi import APIRouter, HTTPException, status, Body
import bcrypt

from api.models import LoginRequestModel, ResponseModel, ErrorResponseModel, create_response, create_error_response

router = APIRouter(
    tags=["Login"],
    prefix="/api/identity/login",
    responses={
        501 : {
            "description" : "Not Implemented Error",
            "model" : ErrorResponseModel
        }
    }
)

@router.post(path='/user',
             description="Uwierzytelnienie użytkownika",
             response_model=ResponseModel)
def user_login(data : LoginRequestModel = Body(...)):
    user_data = {
        "email" : data.email,
        "passwd_hash" : bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()).decode(),
    }
    
    # TODO: DB Driver communication -> checkUserExistance
    return create_error_response(
            status=status.HTTP_501_NOT_IMPLEMENTED,
            message="User authenticate operation not implemented yet",
            detail="Not implemented yet!"
    )
    
    return create_response(status=status.HTTP_200_OK, message="User successfully authenticated.", data=user_data)

@router.post(path='/company',
             description="Uwierzytelnienie przedsiębiorstwa",
             response_model=ResponseModel)
def company_login(data : LoginRequestModel = Body(...)):
    user_data = {
        "email" : data.email,
        "passwd_hash" : bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()).decode(),
    }
    
    # TODO: DB Driver communication -> checkUserExistance
    return create_error_response(
            status=status.HTTP_501_NOT_IMPLEMENTED,
            message="User authenticate operation not implemented yet",
            detail="Not implemented yet!"
    )
    
    return create_response(status=status.HTTP_200_OK, message="User successfully authenticated.", data=user_data)
