from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)


@router.post(path="/token")
def generate_token():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )

@router.get(path="/validate")
def generate_token():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )