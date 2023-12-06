from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/password",
    tags=["Password"]
)


@router.post(path="/reset")
def reset_password():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )

@router.post(path="/change")
def change_password():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )
    
@router.post(path="/forgot")
def forgot_password():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )