from fastapi import FastAPI
from app.routers import modification

app = FastAPI()

app.include_router(modification.router, prefix = "/modify", tags = ["modification"])