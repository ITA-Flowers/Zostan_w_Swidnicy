from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse

from api.models import ResponseModel, ErrorResponseModel, create_response, create_error_response

router = APIRouter(
    tags=["Jobs"],
    prefix="/api/db_driver/jobs",
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
