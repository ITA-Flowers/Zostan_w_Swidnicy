from pydantic import BaseModel
from models import cv

class User(BaseModel):
    username : str
    email : str
    password : str
    user_cv : cv
