from sqlalchemy.orm import Session

# ------------------------------------------------------------------------------------------------
# -- Models
from models import schemas
from models import tables

# ------------------------------------------------------------------------------------------------
# -- GET - read by ID
def get_worker(db : Session, worker_id : int):
    return db.query(tables.Worker).filter(tables.Worker.id == worker_id).first()

# -- GET - read by USER
def get_worker_by_user(db : Session, user: schemas.User):
    return db.query(tables.Worker).filter(tables.Worker.FK_User_uuid == user.uuid).first()

# ------------------------------------------------------------------------------------------------
# -- GET - read many
def get_workers(db : Session, skip : int = 0, limit : int = 100):
    return db.query(tables.Worker).offset(skip).limit(limit).all()

# ------------------------------------------------------------------------------------------------
# -- POST - create
def create_worker(db : Session, worker : schemas.WorkerCreate):
    new_worker = tables.Worker(
        name=worker.name,
        surname=worker.surname,
        profile_img=worker.profile_img,
        user=worker.user
    )
    
    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)
    return new_worker

# ------------------------------------------------------------------------------------------------
# -- DELETE - remove
def delete_worker(db : Session, db_worker : tables.Worker):
    db.delete(db_worker)
    db.commit()
    return db_worker

# ------------------------------------------------------------------------------------------------
# -- PUT - update
def update_worker(db : Session, db_worker : tables.Worker, worker : schemas.Worker):
    worker_data = worker.model_dump(exclude_unset=True)
    for key, value in worker_data.items():
        setattr(db_worker, key, value)
    db.commit()
    db.refresh(db_worker)
    return db_worker
