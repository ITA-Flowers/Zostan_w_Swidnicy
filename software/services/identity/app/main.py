from api.conf import HOST, PORT
from api import init_api

# Inicjalizacja aplikacji FastAPI
app = init_api()

# Uruchomienie aplikacji
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
