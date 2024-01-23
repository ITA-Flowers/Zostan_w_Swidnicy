from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from crud import workers as crud
from database import get_db
from models import schemas


router = APIRouter(
    prefix="/api/workers",
    tags=["Workers"]
)


@router.get(path='/', response_model=list[schemas.Worker])
def get_workers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[schemas.Worker]:
    workers: list[schemas.Worker] = crud.get_workers(db, skip, limit)
    return workers

@router.get(path='/{worker_id}', response_model=schemas.Worker)
def get_worker(worker_id : int, db: Session = Depends(get_db)) -> schemas.Worker:
    worker = crud.get_worker(db, worker_id)
    if worker:
        return worker
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Worker not found!"
    )

@router.post(path='/', response_model=schemas.Worker)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)) -> schemas.Worker:
    return crud.create_worker(db, worker)

@router.put(path='/', response_model=schemas.Worker)
def update_worker(worker: schemas.WorkerUpdate, db: Session = Depends(get_db)) -> schemas.Worker:
    db_worker = crud.get_worker(db, worker.id)
    if not db_worker:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Worker with provided ID does not exists!"
        )
    return crud.update_worker(db, db_worker, worker)

@router.delete(path='/', response_model=schemas.Worker)
def delete_worker(worker: schemas.Worker, db: Session = Depends(get_db)) -> schemas.Worker:
    db_worker = crud.get_worker(db, worker.id)
    if not db_worker:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Worker with provided ID does not exists!"
        )
    return crud.delete_Worker(db, db_worker)
