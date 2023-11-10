from pydantic import BaseModel
from datetime import date
from uuid import UUID
from enum import Enum

from api.schemas import JobForm


# Skill
class SkillBase(BaseModel):
    name : str


class SkillCreate(SkillBase):
    pass


class Skill(SkillBase):
    id : int
    
    class Config:
        orm_mode = True
    

# Experience
class ExperienceBase(BaseModel):
    company_name    : str
    position        : str
    lokalization    : str | None
    begin_date      : date
    end_date        : date | None


class ExperienceCreate(ExperienceBase):
    job_form : JobForm


class Experience(ExperienceBase):
    id : int
    
    report_id   : int
    job_form_id : int

    class Config:
        orm_mode = True


# Education
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
    specialization  : str | None
    begin_date      : date
    end_date        : date | None
    
    
class EducationCreate(EducationBase):
    pass


class Education(EducationBase):
    id          : int
    report_id   : int
    is_current  : bool
    
    class Config:
        orm_mode = True


# Report
class ReportBase(BaseModel):
    address : str
    date_of_birth : date
    
    user_skills     : list[Skill]           = []
    user_experience : list[Experience]  = []
    user_education  : list[Education]   = []
    

class ReportCreate(ReportBase):
    pass
    

class Report(ReportBase):
    id : int
    
    owner_uuid : UUID
    
    class Config:
        orm_mode = True
