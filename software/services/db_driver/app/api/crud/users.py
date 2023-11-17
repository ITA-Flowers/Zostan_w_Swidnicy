from sqlalchemy.orm import Session
from uuid import UUID

from .. import models
from .. import schemas


def get_user(db : Session, user_uuid : UUID):
    return db.query(models.User).filter(models.User.uuid == user_uuid).first()


def get_user_by_email(db : Session, email : str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db : Session, skip : int = 0, limit : int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db : Session, user : schemas.UserCreate):
    new_user = models.User(
        email=user.email,
        passwordHash=user.password_hash,
        passwordSalt=user.password_salt,
        phoneNumber=user.phone_number,
        name=user.name,
        surname=user.surname
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete_user(db : Session, db_user : models.User):
    db.delete(db_user)
    db.commit()
    return db_user


def update_user(db : Session, db_user : models.User, user : schemas.User):
    user_data = user.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user
