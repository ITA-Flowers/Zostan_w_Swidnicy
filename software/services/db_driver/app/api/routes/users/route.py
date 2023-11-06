from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse

from api.models import ResponseModel, ErrorResponseModel, create_response, create_error_response

router = APIRouter(
    tags=["Users"],
    prefix="/api/db_driver/users",
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


@router.get(path='/email',
             description="Znalezienie i pobranie użytkownika po adresie email",
             response_model=ResponseModel)
def get_user_by_email(email : str):
    return create_error_response(
            status=status.HTTP_501_NOT_IMPLEMENTED,
            message="GetUserByEmail : operation not implemented yet",
            detail="Not implemented yet!"
    )


@router.get(path='/phone',
             description="Znalezienie i pobranie użytkownika po adresie email",
             response_model=ResponseModel)
def get_user_by_phone_number(phone_number : str):
    return create_error_response(
            status=status.HTTP_501_NOT_IMPLEMENTED,
            message="GetUserByPhoneNumber : operation not implemented yet",
            detail="Not implemented yet!"
    )
