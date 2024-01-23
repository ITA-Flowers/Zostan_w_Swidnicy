from sqlalchemy.orm import Session
from uuid import UUID

# ------------------------------------------------------------------------------------------------
# -- Models
from ..models import schemas
from ..models import tables

# ------------------------------------------------------------------------------------------------
# -- GET - read by UUID
def get_user(db : Session, user_uuid : UUID):
    return db.query(tables.User).filter(tables.User.uuid == user_uuid).first()

# ------------------------------------------------------------------------------------------------
# -- GET - read by email
def get_user_by_email(db : Session, email : str):
    return db.query(tables.User).filter(tables.User.email == email).first()

# ------------------------------------------------------------------------------------------------
# -- GET - read many
def get_users(db : Session, skip : int = 0, limit : int = 100):
    return db.query(tables.User).offset(skip).limit(limit).all()

# ------------------------------------------------------------------------------------------------
# -- POST - create
def create_user(db : Session, user : schemas.UserCreate):
    new_user = tables.User(
        email=user.email,
        password=user.password,
        phone_number=user.phone_number,
        is_company=user.is_company,
        is_admin=user.is_admin
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ------------------------------------------------------------------------------------------------
# -- DELETE - remove
def delete_user(db : Session, db_user : tables.User):
    db.delete(db_user)
    db.commit()
    return db_user

# ------------------------------------------------------------------------------------------------
# -- PUT - update
def update_user(db : Session, db_user : tables.User, user : schemas.User):
    user_data = user.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user
