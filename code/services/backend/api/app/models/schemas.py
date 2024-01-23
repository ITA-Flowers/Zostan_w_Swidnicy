from pydantic import BaseModel
from uuid import UUID, uuid4
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

# -----------------------------------------------------------------
# -- User
class UserBase(BaseModel):
    email           : str
    phone_number    : str | None = None
    is_company      : bool
    is_admin        : bool

class UserCreate(UserBase):
    password        : str
    
class UserUpdate(UserBase):
    uuid            : UUID

class User(UserBase):
    uuid            : UUID

    class Config:
        from_attributes = True

# -----------------------------------------------------------------
# -- Company
class CompanyBase(BaseModel):
    nip                 : str
    name                : str
    description         : str | None = None
    address             : str | None = None
    logo_img            : bytes | None = None

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
    address             : str | None = None
    description         : str | None = None
    opportunities       : str | None = None
    expire_date         : date | None = None
    img                 : bytes | None = None

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
    salary_min          : int | None = None
    salary_max          : int | None = None
    responsibilities    : str
    description         : str | None = None
    expire_date         : date | None = None
    img                 : bytes | None = None

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
    name                : str | None = None
    surname             : str | None = None
    profile_img         : bytes | None = None

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
    address             : str | None = None

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
    specialization      : str | None = None
    begin_date          : date
    end_date            : date | None = None
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
    end_date            : date | None = None
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