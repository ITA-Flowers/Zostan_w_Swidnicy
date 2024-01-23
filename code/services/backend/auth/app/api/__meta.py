TITLE = "Auth Service"

DESCRIPTION = """

### **#Zostań_w_Świdnicy** - moduł API mikrousługi *Auth*.

Jednostka uwierzytelniania i autoryzacji.

Usługa implementuje i udostępnia interfejs do operacji uwierzytelniania i autoryzacji użytkowników

"""

VERSION = "1.0.0"

OPENAPI_URL = "/api/v1/auth/openapi.json"

TAGS_METADATA = [  
    {
        "name" : "Auth",
        "description" : "Autoryzacja użytkowników"
    },  
    {
        "name" : "Sign",
        "description" : "Uwierzytelnianie zarejestrowanych użytkowników"
    },
    {
        "name" : "Token",
        "description" : "Obsługa tokenów JWT"
    },
]
