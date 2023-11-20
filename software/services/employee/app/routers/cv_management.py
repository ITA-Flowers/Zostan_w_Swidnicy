from fastapi import APIRouter, HTTPException
from models import cv

router = APIRouter()

@router.get("/getcv")
def get_cv(cv_id : int):
    # TODO: pobranie cv o danym ID z DB
    return cv

@router.post("/")
def create_cv(cv : cv, user_id : int):
    # TODO: Utworzenie obiektu CV, strzelenie nim na DB
    return cv

@router.delete("/{cv_id}")
def delete_cv(cv_id: int):
    # TODO: Wywalenie cv o danych id z bazy danych
    return {"message": f"CV {cv_id} deleted successfully"}

@router.put("/{cv_id}")
def update_cv(cv_id : int):
    # TODO aktualizacja danego cv
    return {"message": f"CV {cv_id} updated successfully"}
