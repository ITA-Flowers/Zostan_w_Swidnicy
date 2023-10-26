from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.post("/user", response_model = User)
def user_modify(user : User):
    # TODO: Strzał na DB Driver Service z nowymi danymi użytkownika.

@router.post("/cv", response_model = Cv)
def cv_modify(cv : Cv, user : User):
    # TODO: Obsługa przyjęcia danych do CV, strzał na DB Driver Service