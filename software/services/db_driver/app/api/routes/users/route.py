from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse


router = APIRouter(
    tags=["Users"],
    prefix="/api/db_driver/users"
)
