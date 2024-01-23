from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/companies",
    tags=["Companies"]
)

@router.get(path='/{company_id}')
def get_company(company_id : int):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )