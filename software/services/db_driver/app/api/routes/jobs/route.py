from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse


router = APIRouter(
    tags=["Jobs"],
    prefix="/api/db_driver/jobs"
)
