from fastapi import FastAPI

# Inicjalizacja aplikacji FastAPI
app = FastAPI()

# Przykładowy endpoint
@app.get("/")
def read_root():
    return {"message": "Witaj, to jest przykładowa aplikacja FastAPI!"}

# Inny endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

# Uruchomienie aplikacji
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)