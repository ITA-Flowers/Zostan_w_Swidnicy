from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)

@router.post(path='/authorize')
def authorize():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )