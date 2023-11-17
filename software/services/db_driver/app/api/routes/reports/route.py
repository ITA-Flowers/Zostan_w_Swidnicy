from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse


router = APIRouter(
    tags=["Reports"],
    prefix="/api/db_driver/reports"
)
