from fastapi import FastAPI
from app.routers import

app = FastAPI()

app.include_router(authentication.router, prefix = "/auth", tags = ["authentication"])