from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import auth_router, sign_router, token_router
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

    api.include_router(auth_router)
    api.include_router(sign_router)
    api.include_router(token_router)
    
    return api