from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/jobs",
    tags=["Jobs"]
)

@router.get(path='/{job_id}')
def get_job(job_id : int):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )