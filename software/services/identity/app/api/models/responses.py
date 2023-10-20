from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse


class ResponseModel(BaseModel):
    code    : int = Field(..., description="Response's status code")
    message : str = Field(..., description="Response's details")
    data    : dict = Field(..., description="Response's data structure")
    
    def dict(self):
        return {
            "code" : self.code,
            "message" : self.message,
            "data" : self.data
        }
    
class ErrorResponseModel(BaseModel):
    code    : int = Field(..., description="Response's status code")
    message : str = Field(..., description="Response's error message")
    detail  : str = Field(..., description="Response's error details")
    
    def dict(self):
        return {
            "code" : self.code,
            "message" : self.message,
            "detail" : self.detail
        }
    

def create_response(status : int, message : str, data : dict) -> ResponseModel:
    return ResponseModel(code = status, message = message, data = data)

def create_error_response(status : int, message : str, detail : str) -> ErrorResponseModel:
    return JSONResponse(
        status_code=status,
        content=ErrorResponseModel(code=status, 
                                   message=message,
                                   detail=detail
        ).dict()
    )