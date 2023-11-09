TITLE = "Identity Service"

DESCRIPTION = """

### **#Zostań_w_Świdnicy** - moduł API mikrousługi *Identity*.

Jednostka uwierzytelniania, autoryzacji i rejestracji.

Usługa implementuje i udostępnia interfejs do operacji logowania i rejestracji użytkowników oraz 
podstawowych operacji utwardzających działanie platformy takich jak tokeny JWT.

"""

VERSION = "1.0.0"

TAGS_METADATA = [  
    {
        "name" : "Auth",
        "description" : "Autoryzacja użytkowników, obsługa tokenów JWT - protokół OAuth 2.0"
    },  
    {
        "name" : "Login",
        "description" : "Uwierzytelnianie zarejestrowanych użytkowników"
    },
    {
        "name" : "Register",
        "description" : "Rejestracja nowych użytkowników"
    },
    {
        "name" : "Password",
        "description" : "Resetowanie i zmiana hasła użytkowników"
    },
]
