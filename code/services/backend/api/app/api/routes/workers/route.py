from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/workers",
    tags=["Workers"]
)

@router.get(path='/{worker_id}')
def get_worker(worker_id : int):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )