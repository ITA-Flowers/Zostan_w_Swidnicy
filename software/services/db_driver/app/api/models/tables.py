from sqlalchemy import (Column, 
                        ForeignKey,
                        String, 
                        Boolean, 
                        Date, 
                        Enum,
                        UUID)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.mysql import INTEGER


from database import Base


class User(Base):
    __tablename__ = 'Users'
    
    uuid = Column(UUID(as_uuid=True), primary_key=True, server_default=text("UUID()"), comment='Auto-generated Unique User ID')
    email = Column(String(80), nullable=False, unique=True, comment="User's e-mail address")
    passwordHash = Column(String(255), nullable=False, comment="Hash of user's password")
    phoneNumber = Column(String(20), nullable=True, comment="User's phone number")
    name = Column(String(40), nullable=True, comment="User's name")
    surname = Column(String(60), nullable=True, comment="User's surname")
    
    reports = relationship('Report', backref='user', cascade="all, delete-orphan")
    courses = relationship('CourseParticipant', backref='user', cascade="all, delete-orphan")
    job_applicantions = relationship('JobApplicant', backref='user', cascade="all, delete-orphan")


class Report(Base):
    __tablename__ = 'Reports'
    
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    FK_userUUID = Column(UUID(as_uuid=True), ForeignKey('Users.uuid'), nullable=False)
    address = Column(String(255), nullable=False, comment='Address')
    dateOfBirth = Column(Date, nullable=False, comment="User's date of birth")
    
    user_skills = relationship('UserSkill', backref='report', cascade="all, delete-orphan")
    user_experience = relationship('UserExperience', backref='report', cascade="all, delete-orphan")
    user_education = relationship('UserEducation', backref='report', cascade="all, delete-orphan")


class UserSkill(Base):
    __tablename__ = 'UsersSkills'
    
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    FK_reportId = Column(INTEGER, ForeignKey('Reports.id'), nullable=False)
    FK_skillId = Column(INTEGER, ForeignKey('Skills.id'), nullable=False)
    

class UserExperience(Base):
    __tablename__ = 'UsersExperience'
    
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    FK_jobFormId = Column(INTEGER, ForeignKey('JobForms.id'), nullable=False)
    FK_reportId = Column(INTEGER, ForeignKey('Reports.id'), nullable=False)
    companyName = Column(String(80), nullable=False, comment="Company's name")
    position = Column(String(80), nullable=False, comment="Job position")
    localization = Column(String(255), nullable=True)
    isCurrent = Column(Boolean, nullable=False, comment="Is employee still working there")
    beginDate = Column(Date, nullable=False, comment="Work's date of beginning")
    endDate = Column(Date, nullable=True, comment="Work's date of end")
    
    
class UserEducation(Base):
    __tablename__ = 'UsersEducation'
    
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    FK_reportId = Column(INTEGER, ForeignKey('Reports.id'), nullable=False)
    level = Column(Enum('primary', 'secondary', 'higher', 'bachelor', 'master', 'doctorate', 'vocational', 'continuing'), nullable=False, comment='Education level')
    school = Column(String(255), nullable=False, comment='Finished school name')
    specialization = Column(String(80), nullable=True, comment='Specialization')
    isCurrent = Column(Boolean, nullable=False, comment="Is user still studying there")
    beginDate = Column(Date, nullable=False, comment="Education's date of beginning")
    endDate = Column(Date, nullable=True, comment="Education's date of end")
    

class Course(Base):
    __tablename__ = 'Courses'
    
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    FK_companyNip = Column(String(13), ForeignKey('Companies.nip'), nullable=False)
    name = Column(String(255), nullable=False, comment="Course's name")
    places = Column(INTEGER, nullable=False, comment='Available places')
    isOnline = Column(Boolean, nullable=False, comment='Is it course online')
    
    skills_to_learn = relationship('SkillToLearn', backref='course', cascade="all, delete-orphan")
    course_participants = relationship('CourseParticipant', backref='course', cascade="all, delete-orphan")


class Skill(Base):
    __tablename__ = 'Skills'
    
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, comment="Skill's name")
    
    users_skills = relationship('UserSkill', backref='skill', cascade="all, delete-orphan")
    skills_to_learn = relationship('SkillToLearn', backref='skill', cascade="all, delete-orphan")



class SkillToLearn(Base):
    __tablename__ = 'SkillsToLearn'
    
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    FK_courseId = Column(INTEGER(unsigned=True), ForeignKey('Courses.id'), nullable=False)
    FK_skillId = Column(INTEGER(unsigned=True), ForeignKey('Skills.id'), nullable=False)


class CourseParticipant(Base):
    __tablename__ = 'CourseParticipants'
    
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    FK_courseId = Column(INTEGER(unsigned=True), ForeignKey('Courses.id'), nullable=False)
    FK_userUUID = Column(UUID(as_uuid=True), ForeignKey('Users.uuid'), nullable=False)


class JobApplicant(Base):
    __tablename__ = 'JobApplicants'
    
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    FK_jobOfferId = Column(INTEGER(unsigned=True), ForeignKey('JobOffers.id'), nullable=False)
    FK_userUUID = Column(UUID(as_uuid=True), ForeignKey('Users.uuid'), nullable=False)
    

class JobOffer(Base):
    __tablename__ = 'JobOffers'
    
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    FK_jobFormId = Column(INTEGER(unsigned=True), ForeignKey('JobForms.id'), nullable=False)
    FK_companyNip = Column(String(13), ForeignKey('Companies.nip'), nullable=False)
    name = Column(String(255), nullable=False, comment="Job's name")
    isOnline = Column(Boolean, nullable=False, comment='Is it remote job')
    
    job_applicants = relationship('JobApplicant', backref='job_offer', cascade="all, delete-orphan")


class Company(Base):
    __tablename__ = 'Companies'
    
    nip = Column(String(13), primary_key=True, comment="Company's NIP number")
    FK_categoryId = Column(INTEGER(unsigned=True), ForeignKey('CategoriesOfCompany.id'), nullable=True)
    name = Column(String(80), nullable=False, comment="Company's name")
    email = Column(String(80), nullable=False, comment="Company's e-mail address")
    passwordHash = Column(String(255), nullable=False, comment="Hash of company's password")
    phoneNumber = Column(String(20), nullable=True, comment="Company's phone number")
    
    courses = relationship('Course', backref='company', cascade="all, delete-orphan")
    job_offers = relationship('JobOffer', backref='company', cascade="all, delete-orphan")



class CategoryOfCompany(Base):
    __tablename__ = 'CategoriesOfCompany'
    
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False, comment="Company's category")
    
    companies = relationship('Company', backref='category_of_company')


class JobForm(Base):
    __tablename__ = 'JobForms'
    
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    
    job_offers = relationship('JobOffer', backref='job_form')
    users_experience = relationship('UserExperience', backref='job_form')
