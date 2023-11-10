from pydantic import BaseModel

from api.schemas import User, Skill


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
        orm_mode = True