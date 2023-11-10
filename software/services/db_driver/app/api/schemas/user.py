from pydantic import BaseModel
from uuid import UUID

from api.schemas import Report


class UserBase(BaseModel):
    email           : str
    phone_number    : str | None
    name            : str | None
    surname         : str | None
    

class UserCreate(UserBase):
    password        : str
    

class User(UserBase):
    uuid : UUID
    
    reports : list[Report] = []
    
    class Config:
        orm_mode = True