import bcrypt
import requests
from fastapi import APIRouter, HTTPException, status, Body

import api.models as models
import api.schemas as schemas
from conf.config import settings


router = APIRouter(
    tags=["Register"],
    prefix="/api/identity/register",
)

@router.post(path='/',
             status_code=status.HTTP_201_CREATED,
             description="Rejestracja nowego użytkownika",
             response_model=schemas.User,
             response_description="User successfully created",
             responses={
                 400: {
                    "model": schemas.ErrorResponseDefault,
                    "description": "Error : Email already taken",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Email already taken!"}
                        }
                    },
                }
             })
def user_register(data : models.RegisterRequestModel = Body(...)):
    passwd_salt : bytes = bcrypt.gensalt()
    passwd_hash : bytes = bcrypt.hashpw(data.password.encode(), passwd_salt)
    
    payload = schemas.UserCreate(
        email=data.email,
        password_salt=passwd_salt.decode(),
        password_hash=passwd_hash.decode(),
        phone_number=data.phone_number,
        name=data.name,
        surname=data.surname
    ).model_dump()
    
    url = f'http://{settings.db_drv_host}:{settings.db_drv_port}{settings.db_drv_prefix}/users'
    
    response = requests.post(url=url, json=payload)
    
    if response.status_code == status.HTTP_201_CREATED:
        return response.json()
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json()["detail"]
        )