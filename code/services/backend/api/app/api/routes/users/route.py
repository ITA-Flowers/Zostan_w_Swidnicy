from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from uuid import UUID

from crud import users as crud
from database import get_db
from models import schemas

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)


@router.get(path='/', response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[schemas.User]:
    users: list[schemas.User] = crud.get_users(db, skip, limit)
    return users

@router.get(path='/{user_uuid}', response_model=schemas.User)
def get_user(user_uuid : UUID, db: Session = Depends(get_db)) -> schemas.User:
    user = crud.get_user(db, user_uuid)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found!"
    )

@router.post(path='/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> schemas.User:
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="E-mail address already taken!"
        )
    return crud.create_user(db, user)

@router.put(path='/', response_model=schemas.User)
def update_user(user: schemas.UserUpdate, db: Session = Depends(get_db)) -> schemas.User:
    db_user = crud.get_user(db, user.uuid)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with provided UUID does not exists!"
        )
    return crud.update_user(db, db_user, user)

@router.delete(path='/', response_model=schemas.User)
def delete_user(user: schemas.User, db: Session = Depends(get_db)) -> schemas.User:
    db_user = crud.get_user(db, user.uuid)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with provided UUID does not exists!"
        )
    return crud.delete_user(db, db_user)
