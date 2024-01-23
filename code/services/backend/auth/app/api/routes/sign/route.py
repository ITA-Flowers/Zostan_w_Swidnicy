from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/sign",
    tags=["Sign"]
)

@router.post(path='/logout')
def logout():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )