from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse


router = APIRouter(
    tags=["Companies"],
    prefix="/api/db_driver/companies"
)
