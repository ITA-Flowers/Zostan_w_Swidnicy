from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import companies_router, courses_router, identity_router, jobs_router, reports_router, users_router, workers_router
from .__meta import (TITLE, DESCRIPTION, VERSION, OPENAPI_URL, TAGS_METADATA)


def init_api() -> FastAPI:
    api = FastAPI(
        title=TITLE,
        description=DESCRIPTION,
        version=VERSION,
        OPENAPI_URL=OPENAPI_URL,
        openapi_tags=TAGS_METADATA
    )

    origins = [
    "*",
    ]

    api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    api.include_router(companies_router)
    api.include_router(courses_router)
    api.include_router(identity_router)
    api.include_router(jobs_router)
    api.include_router(reports_router)
    api.include_router(users_router)
    api.include_router(workers_router)
    
    return api