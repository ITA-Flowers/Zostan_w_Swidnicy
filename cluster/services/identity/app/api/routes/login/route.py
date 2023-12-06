from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/login",
    tags=["Login"]
)


@router.post(path="/")
def login():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )

@router.get(path="/status")
def login_status():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )
    
@router.post(path="/out")
def logout():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )
