from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum, BLOB, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid


from .database import Base


class Skill(Base):
    __tablename__ = 'Skills'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)

class User(Base):
    __tablename__ = 'Users'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    password = Column(String(128), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    phone_number = Column(String(20))
    is_company = Column(Boolean, nullable=False)
    is_admin = Column(Boolean, nullable=False)

class Company(Base):
    __tablename__ = 'Companies'

    id = Column(Integer, primary_key=True, index=True)
    FK_User_uuid = Column(UUID(as_uuid=True), ForeignKey('Users.uuid'), nullable=False)
    nip = Column(String(16), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(512))
    address = Column(String(512))
    logo_img = Column(BLOB)

    user = relationship("User")
    
class Course(Base):
    __tablename__ = 'Courses'

    id = Column(Integer, primary_key=True, index=True)
    FK_Company_id = Column(Integer, ForeignKey('Companies.id'), nullable=False)
    title = Column(String(256), nullable=False)
    price = Column(Integer, default=0, nullable=False)
    duration = Column(Integer, nullable=False)
    places = Column(Integer, default=1, nullable=False)
    address = Column(String(512))
    description = Column(String(1024))
    opportunities = Column(String(1024))
    expire_date = Column(Date)
    img = Column(BLOB)
    created_at = Column(Date, default=func.curdate(), nullable=False)

    company = relationship("Company")

class CourseRequirement(Base):
    __tablename__ = 'CourseRequirements'

    id = Column(Integer, primary_key=True, index=True)
    FK_Course_id = Column(Integer, ForeignKey('Courses.id'), nullable=False)
    FK_Skill_id = Column(Integer, ForeignKey('Skills.id'), nullable=False)

    course = relationship("Course")
    skill = relationship("Skill")

class CourseSkill(Base):
    __tablename__ = 'CourseSkills'

    id = Column(Integer, primary_key=True, index=True)
    FK_Course_id = Column(Integer, ForeignKey('Courses.id'), nullable=False)
    FK_Skill_id = Column(Integer, ForeignKey('Skills.id'), nullable=False)

    course = relationship("Course")
    skill = relationship("Skill")

class Job(Base):
    __tablename__ = 'Jobs'

    id = Column(Integer, primary_key=True, index=True)
    FK_Company_id = Column(Integer, ForeignKey('Companies.id'), nullable=False)
    title = Column(String(256), nullable=False)
    working_time = Column(Enum('full-time', 'part-time', 'temporary'), nullable=False)
    contract_type = Column(Enum('employment', 'contract', 'task-specific', 'internship', 'b2b'), nullable=False)
    work_type = Column(Enum('stationary', 'hybrid', 'remote', 'mobile'), nullable=False)
    position = Column(String(80), nullable=False)
    address = Column(String(256), nullable=False)
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    responsibilities = Column(String(1024), nullable=False)
    description = Column(String(1024))
    expire_date = Column(Date)
    img = Column(BLOB)
    created_at = Column(Date, default=func.curdate(), nullable=False)

    company = relationship("Company")

class JobRequirement(Base):
    __tablename__ = 'JobRequirements'

    id = Column(Integer, primary_key=True, index=True)
    FK_Job_id = Column(Integer, ForeignKey('Jobs.id'), nullable=False)
    FK_Skill_id = Column(Integer, ForeignKey('Skills.id'), nullable=False)

    job = relationship("Job")
    skill = relationship("Skill")

class Worker(Base):
    __tablename__ = 'Workers'

    id = Column(Integer, primary_key=True, index=True)
    FK_User_uuid = Column(UUID(as_uuid=True), ForeignKey('Users.uuid'), nullable=False)
    name = Column(String(40))
    surname = Column(String(60))
    profile_img = Column(BLOB)

    user = relationship("User")

class CourseParticipant(Base):
    __tablename__ = 'CourseParticipants'

    id = Column(Integer, primary_key=True, index=True)
    FK_Course_id = Column(Integer, ForeignKey('Courses.id'), nullable=False)
    FK_Worker_id = Column(Integer, ForeignKey('Workers.id'), nullable=False)

    course = relationship("Course")
    worker = relationship("Worker")

class JobApplicant(Base):
    __tablename__ = 'JobApplicants'

    id = Column(Integer, primary_key=True, index=True)
    FK_Job_id = Column(Integer, ForeignKey('Jobs.id'), nullable=False)
    FK_Worker_id = Column(Integer, ForeignKey('Workers.id'), nullable=False)

    job = relationship("Job")
    worker = relationship("Worker")

class Report(Base):
    __tablename__ = 'Reports'

    id = Column(Integer, primary_key=True, index=True)
    FK_Worker_id = Column(Integer, ForeignKey('Workers.id'), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    address = Column(String(512))

    worker = relationship("Worker")

class ReportEducation(Base):
    __tablename__ = 'ReportEducations'

    id = Column(Integer, primary_key=True, index=True)
    FK_Report_id = Column(Integer, ForeignKey('Reports.id'), nullable=False)
    level = Column(Enum('primary', 'secondary', 'bachelor', 'master', 'doctorate', 'vocational', 'continuing'), nullable=False)
    school = Column(String(512), nullable=False)
    specialization = Column(String(128))
    begin_date = Column(Date, nullable=False)
    end_date = Column(Date)
    is_ongoing = Column(Boolean, nullable=False)

    report = relationship("Report")

class ReportExperience(Base):
    __tablename__ = 'ReportExperience'

    id = Column(Integer, primary_key=True, index=True)
    FK_Report_id = Column(Integer, ForeignKey('Reports.id'), nullable=False)
    company_name = Column(String(128), nullable=False)
    position = Column(String(80), nullable=False)
    address = Column(String(512), nullable=False)
    contract_type = Column(Enum('employment', 'contract', 'task-specific', 'internship', 'b2b'), nullable=False)
    work_type = Column(Enum('stationary', 'hybrid', 'remote', 'mobile'), nullable=False)
    begin_date = Column(Date, nullable=False)
    end_date = Column(Date)
    is_ongoing = Column(Boolean, nullable=False)

    report = relationship("Report")

class ReportSkill(Base):
    __tablename__ = 'ReportSkills'

    id = Column(Integer, primary_key=True, index=True)
    FK_Report_id = Column(Integer, ForeignKey('Reports.id'), nullable=False)
    FK_Skill_id = Column(Integer, ForeignKey('Skills.id'), nullable=False)

    report = relationship("Report")
    skill = relationship("Skill")