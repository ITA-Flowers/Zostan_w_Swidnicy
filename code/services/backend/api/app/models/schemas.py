from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import date

from .enums import *


# -----------------------------------------------------------------
# -- Skill
class SkillBase(BaseModel):
    name: str

class SkillCreate(SkillBase):
    pass

class SkillUpdate(SkillBase):
    id: int

class Skill(SkillBase):
    id: int

    class Config:
        from_attributes = True

        json_schema_extra = {
            "example" : {
                "id" : 99,
                "name" : "Programowanie Python"
            }
        }

# -----------------------------------------------------------------
# -- User
class UserBase(BaseModel):
    email           : str
    phone_number    : Optional[str] = None
    is_company      : bool = False
    is_admin        : bool = False

class UserCreate(UserBase):
    password        : str
    
class UserUpdate(UserBase):
    uuid            : UUID

class User(UserBase):
    uuid            : UUID

    class Config:
        from_attributes = True

        json_schema_extra = {
            "example" : {
                "uuid" : "568ade48-b9cf-12ee-9df0-0232ac130002",
                "email" : "adam.abacki@gmail.com",
                "phone_number" : "772546887",
                "is_company" : False,
                "is_admin" : False
            }
        }

# -----------------------------------------------------------------
# -- Company
class CompanyBase(BaseModel):
    nip                 : str
    name                : str
    description         : Optional[str] = None
    address             : Optional[str] = None
    logo_img            : Optional[bytes] = None

class CompanyCreate(CompanyBase):
    user                : User

class CompanyUpdate(CompanyBase):
    id                  : int

class Company(CompanyBase):
    id                  : int
    user                : User
    
    class Config:
        from_attributes = True

# -----------------------------------------------------------------
# -- Course
class CourseBase(BaseModel):
    title               : str
    price               : int
    duration            : int
    places              : int
    address             : Optional[str] = None
    description         : Optional[str] = None
    opportunities       : Optional[str] = None
    expire_date         : Optional[date] = None
    img                 : Optional[bytes] = None

class CourseCreate(CourseBase):
    company             : Company

class CourseUpdate(CourseBase):
    id                  : int

class Course(CourseBase):
    id                  : int
    company             : Company
    created_at          : date

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- Job
class JobBase(BaseModel):
    title               : str
    working_time        : WorkingTimeEnum
    contract_type       : ContractTypeEnum
    work_type           : WorkTypeEnum
    position            : str
    address             : str
    salary_min          : Optional[int] = None
    salary_max          : Optional[int] = None
    responsibilities    : str
    description         : Optional[str] = None
    expire_date         : Optional[date] = None
    img                 : Optional[bytes] = None

class JobCreate(JobBase):
    company             : Company

class JobUpdate(JobBase):
    id                  : int

class Job(JobBase):
    id                  : int
    company             : Company
    created_at          : date

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- Worker
class WorkerBase(BaseModel):
    name                : Optional[str] = None
    surname             : Optional[str] = None
    profile_img         : Optional[bytes] = None

class WorkerCreate(WorkerBase):
    user                : User
    
class WorkerUpdate(WorkerBase):
    id                  : int

class Worker(WorkerBase):
    id                  : int
    user                : User

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- CourseRequirement
class CourseRequirementBase(BaseModel):
    pass

class CourseRequirementCreate(CourseRequirementBase):
    course              : Course
    skill               : Skill

class CourseRequirement(CourseRequirementBase):
    id                  : int
    course              : Course
    skill               : Skill

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- JobRequirement
class JobRequirementBase(BaseModel):
    pass

class JobRequirementCreate(JobRequirementBase):
    job                 : Job
    skill               : Skill

class JobRequirement(JobRequirementBase):
    id                  : int
    job                 : Job
    skill               : Skill

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- CourseParticipant
class CourseParticipantBase(BaseModel):
    pass

class CourseParticipantCreate(CourseParticipantBase):
    course              : Course
    worker              : Worker

class CourseParticipant(CourseParticipantBase):
    id                  : int

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- JobApplicant
class JobApplicantBase(BaseModel):
    pass

class JobApplicantCreate(JobApplicantBase):
    job                 : Job
    worker              : Worker

class JobApplicant(JobApplicantBase):
    id                  : int
    job                 : Job
    worker              : Worker

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- Report
class ReportBase(BaseModel):
    date_of_birth       : date
    address             : Optional[str] = None

class ReportCreate(ReportBase):
    worker              : Worker

class ReportUpdate(ReportBase):
    id                  : int

class Report(ReportBase):
    id                  : int
    worker              : Worker

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- ReportEducation
class ReportEducationBase(BaseModel):
    level               : EducationLevelEnum
    school              : str
    specialization      : Optional[str] = None
    begin_date          : date
    end_date            : Optional[date] = None
    is_ongoing          : bool

class ReportEducationCreate(ReportEducationBase):
    report              : Report

class ReportEducationUpdate(ReportEducationBase):
    id                  : int

class ReportEducation(ReportEducationBase):
    id                  : int
    report              : Report

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- ReportExperience
class ReportExperienceBase(BaseModel):
    company_name        : str
    position            : str
    address             : str
    contract_type       : ContractTypeEnum
    work_type           : WorkTypeEnum
    begin_date          : date
    end_date            : Optional[date] = None
    is_ongoing          : bool

class ReportExperienceCreate(ReportExperienceBase):
    report              : Report

class ReportExperienceUpdate(ReportExperienceBase):
    id                  : int

class ReportExperience(ReportExperienceBase):
    id                  : int
    report              : Report

    class Config:
        from_attributes = True

# -----------------------------------------------------------------
# -- ReportLink
class ReportLinkBase(BaseModel):
    name                : str
    url                 : str
    
class ReportLinkCreate(ReportLinkBase):
    report              : Report
    
class ReportLinkUpdate(ReportLinkBase):
    id                  : int
    
class ReportLink(ReportLinkBase):
    id                  : int
    report              : Report
    
    class Config:
        from_attributes = True

# -----------------------------------------------------------------
# -- ReportCert
class ReportCertBase(BaseModel):
    certname            : str
    hostname            : str
    obtain_date         : date
    
class ReportCertCreate(ReportCertBase):
    report              : Report
    
class ReportCertUpdate(ReportCertBase):
    id                  : int
    
class ReportCert(ReportCertBase):
    id                  : int
    report              : Report
    
    class Config:
        from_attributes = True

# -----------------------------------------------------------------
# -- ReportSkill
class ReportSkillBase(BaseModel):
    pass

class ReportSkillCreate(ReportSkillBase):
    report              : Report
    skill               : Skill

class ReportSkill(ReportSkillBase):
    id                  : int
    report              : Report
    skill               : Skill

    class Config:
        from_attributes = True