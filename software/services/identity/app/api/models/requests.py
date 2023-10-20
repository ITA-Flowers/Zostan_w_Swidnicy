from pydantic import BaseModel, Field


class LoginRequestModel(BaseModel):
    email       : str = Field(..., description="User's email",      example="user@mailbox.com")
    password    : str = Field(..., description="User's password",   example="Password1")


class RegisterRequestModel(BaseModel):
    email           : str = Field(..., description="User's email",          example="user@mailbox.com")
    password        : str = Field(..., description="User's password",       example="Password1")
    phone_number    : str = Field(..., description="User's phone number",   example="+48524665997")
