from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/api/reports",
    tags=["Reports"]
)

@router.get(path='/{report_id}')
def get_report(report_id : int):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented yet!"
    )