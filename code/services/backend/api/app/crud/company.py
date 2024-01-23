from sqlalchemy.orm import Session

# ------------------------------------------------------------------------------------------------
# -- Models
from models import schemas
from models import tables

# ------------------------------------------------------------------------------------------------
# -- GET - read by ID
def get_company(db : Session, company_id : int):
    return db.query(tables.Company).filter(tables.Company.id == company_id).first()

# -- GET - read by NIP
def get_company_by_nip(db : Session, nip : str):
    return db.query(tables.Company).filter(tables.Company.nip == nip).first()

# -- GET - read by USER
def get_company_by_user(db : Session, user : schemas.User):
    return db.query(tables.Company).filter(tables.Company.FK_User_uuid == user.uuid).first()

# ------------------------------------------------------------------------------------------------
# -- GET - read many
def get_companies(db : Session, skip : int = 0, limit : int = 100):
    return db.query(tables.Company).offset(skip).limit(limit).all()

# ------------------------------------------------------------------------------------------------
# -- POST - create
def create_company(db : Session, company : schemas.CompanyCreate):
    new_company = tables.Company(
        nip=company.nip,
        name=company.name,
        description=company.description,
        address=company.address,
        logo_img=company.logo_img,
        user=company.user
    )
    
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

# ------------------------------------------------------------------------------------------------
# -- DELETE - remove
def delete_company(db : Session, db_company : tables.Company):
    db.delete(db_company)
    db.commit()
    return db_company

# ------------------------------------------------------------------------------------------------
# -- PUT - update
def update_company(db : Session, db_company : tables.Company, company : schemas.Company):
    company_data = company.model_dump(exclude_unset=True)
    for key, value in company_data.items():
        setattr(db_company, key, value)
    db.commit()
    db.refresh(db_company)
    return db_company
