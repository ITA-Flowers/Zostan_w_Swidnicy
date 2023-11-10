from pydantic import BaseModel

from api.schemas import JobOffer, Course


# Company Categories
class CompanyCategoryBase(BaseModel):
    name : str


class CompanyCategoryCreate(CompanyCategoryBase):
    pass


class CompanyCategory(CompanyCategoryBase):
    id : int
    
    class Config:
        orm_mode = True


# Company
class CompanyBase(BaseModel):
    nip             : str
    name            : str
    email           : str
    phone_number    : str | None
    
    job_offers  : list[JobOffer] = []
    courses     : list[Course]  = []
    

class CompanyCreate(CompanyBase):
    password : str
    category : CompanyCategory
    

class Company(CompanyBase):
    category_id : int
    
    class Config:
        orm_mode = True
