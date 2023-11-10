from pydantic import BaseModel
from datetime import date
from uuid import UUID, uuid4
from enum import Enum


# -----------------------------------------------------------------
# -- JobForm
class JobFormBase(BaseModel):
    name : str


class JobFormCreate(JobFormBase):
    pass
    

class JobForm(JobFormBase):
    id : int
    
    class Config:
        from_attributes = True


# -----------------------------------------------------------------
# -- Skill
class SkillBase(BaseModel):
    name : str


class SkillCreate(SkillBase):
    pass


class Skill(SkillBase):
    id : int
    
    class Config:
        from_attributes = True
    

# -----------------------------------------------------------------
# -- Experience
class ExperienceBase(BaseModel):
    company_name    : str
    position        : str
    lokalization    : str  | None = None
    begin_date      : date
    end_date        : date | None = None


class ExperienceCreate(ExperienceBase):
    job_form : JobForm


class Experience(ExperienceBase):
    id : int
    
    report_id   : int
    job_form_id : int

    class Config:
        from_attributes = True


# -----------------------------------------------------------------
# -- Education
class EducationLevel(Enum):
    PRIMARY     = 'Primary'
    SECONDARY   = 'Secondary'
    HIGHER      = 'Higher'
    BACHELOR    = 'Bachelor'
    MASTER      = 'Master'
    DOCTORATE   = 'Doctorate'
    VOCATIONAL  = 'Vocational'
    CONTINUING  = 'Continuing'
    

class EducationBase(BaseModel):
    level           : EducationLevel
    school          : str
    specialization  : str  | None = None
    begin_date      : date
    end_date        : date | None = None
    
    
class EducationCreate(EducationBase):
    pass


class Education(EducationBase):
    id          : int
    report_id   : int
    is_current  : bool
    
    class Config:
        from_attributes = True


# -----------------------------------------------------------------
# -- Report
class ReportBase(BaseModel):
    address : str
    date_of_birth : date
    
    user_skills     : list[Skill]       = []
    user_experience : list[Experience]  = []
    user_education  : list[Education]   = []
    

class ReportCreate(ReportBase):
    pass
    

class Report(ReportBase):
    id : int
    
    owner_uuid : UUID
    
    class Config:
        from_attributes = True

# -----------------------------------------------------------------
# -- User
class UserBase(BaseModel):
    email           : str
    phone_number    : str | None = None
    name            : str | None = None
    surname         : str | None = None
    

class UserCreate(UserBase):
    password_hash   : str
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "email": "j.doe@gmail.com",
                "password_hash": "$6$8MpO8TKre4VgAEwj$foglImF2sDpTTZScuIoQdXkX3jb9jrrawEnu/TdetciApBAVXJ41x1XW43/9QwnJfBoNrz9OabksRqsitFUOO1",
                "phone_number": "321546879",
                "name": "John",
                "surname": "Doe"
            }
        }
        

class User(UserBase):
    uuid : UUID
    
    reports : list[Report] = []
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "uuid": str(uuid4()),
                "email": "j.doe@gmail.com",
                "phone_number": "321546879",
                "name": "John",
                "surname": "Doe",
                "reports": []
            }
        }


# -----------------------------------------------------------------
# -- JobOffer
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
        from_attributes = True


# -----------------------------------------------------------------
# -- Course
class CourseBase(BaseModel):
    name        : str
    places      : int
    is_online   : bool
    
    paricipants     : list[User]  = []
    skills_to_learn : list[Skill] = []
    

class CourseCreate(CourseBase):
    pass
    

class Course(CourseBase):
    id : int
    
    class Config:
        from_attributes = True


# -----------------------------------------------------------------
# -- Company Categories
class CompanyCategoryBase(BaseModel):
    name : str


class CompanyCategoryCreate(CompanyCategoryBase):
    pass


class CompanyCategory(CompanyCategoryBase):
    id : int
    
    class Config:
        from_attributes = True


# -----------------------------------------------------------------
# -- Company
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
        from_attributes = True
