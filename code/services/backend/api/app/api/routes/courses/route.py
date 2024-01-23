from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/courses",
    tags=["Courses"]
)

@router.get(path='/{course_id}')
def get_course(course_id : int):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )