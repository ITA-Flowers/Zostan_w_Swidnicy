from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse


router = APIRouter(
    tags=["Courses"],
    prefix="/api/db_driver/courses"
)
