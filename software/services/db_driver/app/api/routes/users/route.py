from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from uuid import UUID

import api.schemas as schemas
import api.crud.users as crud
from database import SessionLocal


router = APIRouter(
    tags=["Users"],
    prefix="/api/db_driver/users"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.post(path="/", 
             status_code=status.HTTP_201_CREATED, 
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
def create_user(user : schemas.UserCreate, db : Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already taken!"
        )
    return crud.create_user(db, user=user)


@router.get(path="/{user_uuid}", 
            response_model=schemas.User, 
            response_description="User found",
            responses={
                 404: {
                    "model": schemas.ErrorResponseDefault,
                    "description": "Error : User not found",
                    "content": {
                        "application/json": {
                            "example": {"detail": "User not found!"}
                        }
                    },
                }
             })
def read_user(user_uuid : UUID, db : Session = Depends(get_db)):
    db_user = crud.get_user(db, user_uuid=user_uuid)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )
    return db_user


@router.put(path="/",
             response_model=schemas.User, 
             response_description="User successfully updated",
             responses={
                 400: {
                    "model": schemas.ErrorResponseDefault,
                    "description": "Error : Email already taken",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Email already taken!"}
                        }
                    },
                },
                 404: {
                    "model": schemas.ErrorResponseDefault,
                    "description": "Error : User not found",
                    "content": {
                        "application/json": {
                            "example": {"detail": "User not found!"}
                        }
                    },
                }
             })
def update_user(user : schemas.User, db : Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )
    
    if db_user.uuid != user.uuid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already taken!"
        )
    return crud.update_user(db, db_user=db_user, user=user)


@router.delete(path="/{user_uuid}",
               response_model=schemas.User, 
               response_description="User successfully deleted",
               responses={
                    404: {
                       "model": schemas.ErrorResponseDefault,
                       "description": "Error : User not found",
                       "content": {
                           "application/json": {
                               "example": {"detail": "User not found!"}
                           }
                       },
                   }
                })
def delete_user(user_uuid : UUID, db : Session = Depends(get_db)):
    db_user = crud.get_user(db, user_uuid=user_uuid)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )
    return crud.delete_user(db, db_user=db_user)


@router.get(path="/", response_model=list[schemas.User])
def read_users(skip : int = 0, limit : int = 100, db : Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
