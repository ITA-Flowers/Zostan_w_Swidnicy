from pydantic import BaseModel


class ErrorResponseDefault(BaseModel):
    detail : str
