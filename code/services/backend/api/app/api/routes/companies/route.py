from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from crud import company as crud
from crud import users as crud_users
from database import get_db
from models import schemas


router = APIRouter(
    prefix="/api/companies",
    tags=["Companies"]
)


@router.get(path='/', response_model=list[schemas.Company])
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[schemas.Company]:
    companies: list[schemas.Company] = crud.get_companies(db, skip, limit)
    return companies

@router.get(path='/{company_id}', response_model=schemas.Company)
def get_company(company_id : int, db: Session = Depends(get_db)) -> schemas.Company:
    company = crud.get_company(db, company_id)
    if company:
        return company
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Company not found!"
    )

@router.post(path='/', response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)) -> schemas.Company:
    return crud.create_company(db, company)

@router.put(path='/', response_model=schemas.Company)
def update_company(company: schemas.CompanyUpdate, db: Session = Depends(get_db)) -> schemas.Company:
    db_company = crud.get_company(db, company.id)
    if not db_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company with provided ID does not exists!"
        )
    return crud.update_company(db, db_company, company)

@router.delete(path='/', response_model=schemas.Company)
def delete_company(company: schemas.Company, db: Session = Depends(get_db)) -> schemas.Company:
    db_company = crud.get_company(db, company.id)
    if not db_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company with provided ID does not exists!"
        )
    return crud.delete_Company(db, db_company)
