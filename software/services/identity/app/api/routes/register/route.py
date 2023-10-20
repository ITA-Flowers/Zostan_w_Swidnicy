from fastapi import APIRouter, HTTPException, status, Body
import bcrypt

from fastapi.responses import JSONResponse

from api.models import RegisterRequestModel, ResponseModel, ErrorResponseModel, create_response, create_error_response

router = APIRouter(
    tags=["Identity"],
    prefix="/api/identity/register",
    responses={
        409 : {
            "description" : "Conflict Error",
            "model" : ErrorResponseModel
        },
        501 : {
            "description" : "Not Implemented Error",
            "model" : ErrorResponseModel
        }
    }
)

@router.post(path='/user',
             description="Rejestracja nowego użytkownika",
             response_model=ResponseModel)
def user_register(data : RegisterRequestModel = Body(...)):
    user_data = {
        "email" : data.email,
        "passwd_hash" : bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()).decode(),
        "phone_number" : data.phone_number
    }
    
    # TODO: DB Driver communication -> checkUserExistance, addUserToDB
    return create_error_response(
            status=status.HTTP_501_NOT_IMPLEMENTED,
            message="User register operation not implemented yet",
            detail="Not implemented yet!"
    )
    
    return create_response(status=status.HTTP_201_CREATED, message="User successfully registered.", data=user_data)