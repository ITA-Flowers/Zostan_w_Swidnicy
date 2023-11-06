from pydantic import BaseModel, Field

class User(BaseModel):
    email           : str = Field(..., description="User's e-mail")
    password        : str = Field(..., description="User's password's hash")
    phone_number    : str = Field(..., description="User's phone number")
