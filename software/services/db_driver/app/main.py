from api import init_api

# Inicjalizacja aplikacji FastAPI
app = init_api()

# Uruchomienie aplikacji
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
