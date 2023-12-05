from pydantic import BaseModel
from typing import Optional, List

# -----------------------------------------------------------------
# -- Skill
class SkillBase(BaseModel):
    name: str

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int

    class Config:
        from_attributes = True

# -----------------------------------------------------------------
# -- User
class UserBase(BaseModel):
    email: str
    phone_number: Optional[str] = None
    is_company: bool
    is_admin: bool

class UserCreate(UserBase):
    password: str

class User(UserBase):
    uuid: str

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- Course
class CourseBase(BaseModel):
    title: str
    price: int
    duration: int
    places: int
    address: Optional[str] = None
    description: Optional[str] = None
    opportunities: Optional[str] = None
    expire_date: Optional[str] = None

class CourseCreate(CourseBase):
    FK_Company_id: int

class Course(CourseBase):
    id: int
    created_at: str

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- Job
class JobBase(BaseModel):
    title: str
    working_time: str
    contract_type: str
    work_type: str
    position: str
    address: str
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    responsibilities: str
    description: Optional[str] = None
    expire_date: Optional[str] = None

class JobCreate(JobBase):
    FK_Company_id: int

class Job(JobBase):
    id: int
    created_at: str

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- Worker
class WorkerBase(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None

class WorkerCreate(WorkerBase):
    FK_User_uuid: str

class Worker(WorkerBase):
    id: int
    profile_img: Optional[bytes] = None

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- CourseRequirement
class CourseRequirementBase(BaseModel):
    FK_Course_id: int
    FK_Skill_id: int

class CourseRequirementCreate(CourseRequirementBase):
    pass

class CourseRequirement(CourseRequirementBase):
    id: int

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- JobRequirement
class JobRequirementBase(BaseModel):
    FK_Job_id: int
    FK_Skill_id: int

class JobRequirementCreate(JobRequirementBase):
    pass

class JobRequirement(JobRequirementBase):
    id: int

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- CourseParticipant
class CourseParticipantBase(BaseModel):
    FK_Course_id: int
    FK_Worker_id: int

class CourseParticipantCreate(CourseParticipantBase):
    pass

class CourseParticipant(CourseParticipantBase):
    id: int

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- JobApplicant
class JobApplicantBase(BaseModel):
    FK_Job_id: int
    FK_Worker_id: int

class JobApplicantCreate(JobApplicantBase):
    pass

class JobApplicant(JobApplicantBase):
    id: int

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- Report
class ReportBase(BaseModel):
    FK_Worker_id: int
    date_of_birth: str
    address: Optional[str] = None

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    id: int

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- ReportEducation
class ReportEducationBase(BaseModel):
    FK_Report_id: int
    level: str
    school: str
    specialization: Optional[str] = None
    begin_date: str
    end_date: Optional[str] = None
    is_ongoing: bool

class ReportEducationCreate(ReportEducationBase):
    pass

class ReportEducation(ReportEducationBase):
    id: int

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- ReportExperience
class ReportExperienceBase(BaseModel):
    FK_Report_id: int
    company_name: str
    position: str
    address: str
    contract_type: str
    work_type: str
    begin_date: str
    end_date: Optional[str] = None
    is_ongoing: bool

class ReportExperienceCreate(ReportExperienceBase):
    pass

class ReportExperience(ReportExperienceBase):
    id: int

    class Config:
        from_attributes = True
        
# -----------------------------------------------------------------
# -- ReportSkill
class ReportSkillBase(BaseModel):
    FK_Report_id: int
    FK_Skill_id: int

class ReportSkillCreate(ReportSkillBase):
    pass

class ReportSkill(ReportSkillBase):
    id: int

    class Config:
        from_attributes = True