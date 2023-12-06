from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/register",
    tags=["Register"]
)


@router.post(path="/worker")
def register_worker():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )

@router.post(path="/company")
def register_company():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )
    
@router.get(path="/verify")
def verify_user():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )