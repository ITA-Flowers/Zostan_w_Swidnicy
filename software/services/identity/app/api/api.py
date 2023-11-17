from fastapi import FastAPI

from .routes import auth_router, login_router, register_router, password_router
from .__meta import (TITLE,
                    DESCRIPTION,
                    VERSION,
                    TAGS_METADATA)
 
'''
 Endpoints:
    1. register : POST : /api/identity/register              : all user data                         : None
    2. login    : POST : /api/identity/login                 : email, password                       : access token, refresh token
    3. login    : POST : /api/identity/logout                : access token                          : None
    4. auth     : POST : /api/identity/refresh               : refresh token                         : access token, refresh token
    5. password : POST : /api/identity/password-change       : old, new passwds, access token        : None
    6. password : POST : /api/identity/password-reset        : email                                 : None
    7. auth     : POST : /api/identity/verify-token          : access token to verification          : token validation status

 Token check:
    1. With `MIDDLEWARE`
'''

def init_api() -> FastAPI:
    api = FastAPI(
        title=TITLE,
        description=DESCRIPTION,
        version=VERSION,
        openapi_tags=TAGS_METADATA
    )
    
    api.include_router(auth_router)
    api.include_router(login_router)
    api.include_router(register_router)
    api.include_router(password_router)
    
    return api