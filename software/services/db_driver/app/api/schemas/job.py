from pydantic import BaseModel
from uuid import UUID

from api.schemas import User


# JobForm
class JobFormBase(BaseModel):
    name : str


class JobFormCreate(JobFormBase):
    pass
    

class JobForm(JobFormBase):
    id : int
    
    class Config:
        orm_mode = True
        

# JobOffer
class JobOfferBase(BaseModel):
    name : str
    is_online : bool
    
    applicants : list[User] = []
    

class JobOfferCreate(JobOfferBase):
    job_form : JobForm
    

class JobOffer(JobOfferBase):
    id : int
    
    job_form_id : int
    company_nip : str
    
    class Config:
        orm_mode = True


