from pydantic import BaseModel
from typing import Dict

class User(BaseModel):
    username : str
    email : str
    password : str
