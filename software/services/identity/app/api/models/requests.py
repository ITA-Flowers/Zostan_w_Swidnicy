from pydantic import BaseModel, Field


class RefreshTokenRequestModel(BaseModel):
    refresh_token : str = Field(..., description="User's refresh token")


class VerifyTokenRequestModel(BaseModel):
    access_token : str = Field(..., description="User's access token")
    
    
class LoginRequestModel(BaseModel):
    email       : str = Field(..., description="User's email",      example="user@mailbox.com")
    password    : str = Field(..., description="User's password",   example="Password1")


class LogoutRequestModel(BaseModel):
    access_token : str = Field(..., description="User's access token")
    
    
class PasswordResetRequestModel(BaseModel):
    email       : str = Field(..., description="User's email",      example="user@mailbox.com")


class PasswordChangeRequestModel(BaseModel):
    old_password    : str = Field(..., description="User's old password",   example="Password1")
    new_password    : str = Field(..., description="User's new password",   example="Password2")
    
    
class RegisterRequestModel(BaseModel):
    email           : str = Field(..., description="User's email",          example="user@mailbox.com")
    password        : str = Field(..., description="User's password",       example="Password1")
    phone_number    : str | None = Field(..., description="User's phone number",   example="+48524665997")
    name            : str | None = Field(..., description="User's name",    example="John")
    surname         : str | None = Field(..., description="User's surname", example="Doe")