from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/token",
    tags=["Token"]
)

@router.post(path='/')
def get_token():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )

@router.post(path='/refresh')
def refresh_token():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )