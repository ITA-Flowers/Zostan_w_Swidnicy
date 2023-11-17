from fastapi import FastAPI

from .__meta import (TITLE,
                    DESCRIPTION,
                    VERSION,
                    TAGS_METADATA)

from .routes import (users_router, 
                     companies_router, 
                     reports_router, 
                     courses_router, 
                     jobs_router)

def init_api() -> FastAPI:
    api = FastAPI(
        title=TITLE,
        description=DESCRIPTION,
        version=VERSION,
        openapi_tags=TAGS_METADATA
    )
        
    api.include_router(users_router)
    api.include_router(companies_router)
    api.include_router(reports_router)
    api.include_router(courses_router)
    api.include_router(jobs_router)
    
    return api