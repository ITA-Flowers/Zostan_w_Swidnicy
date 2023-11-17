from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import date
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
    PRIMARY     = 'primary'
    SECONDARY   = 'secondary'
    HIGHER      = 'higher'
    BACHELOR    = 'bachelor'
    MASTER      = 'master'
    DOCTORATE   = 'doctorate'
    VOCATIONAL  = 'vocational'
    CONTINUING  = 'continuing'
    

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
    password_salt   : str
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "email": "j.doe@gmail.com",
                "password_hash": "$2b$8MpO8TKre4VgAEwjfoglImF2sDpTTZScuIoQdXkX3jb9jrrawEnu/TdetciApBAVXJ41x1XW43/9QwnJfBoNrz9OabksRqsitFUOO1",
                "password_salt": "$2b$8MpO8TKre4VgAEwjfog",
                "phone_number": "521885446",
                "name": "John",
                "surname": "Doe"
            }
        }


class UserUpdate(UserBase):
    uuid : UUID
        
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "uuid": str(uuid4()),
                "email": "j.doe@gmail.com",
                "phone_number": "521885446",
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
                "phone_number": "521885446",
                "name": "John",
                "surname": "Doe",
                "report": []
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
    

class Company(CompanyBase):
    
    class Config:
        from_attributes = True
