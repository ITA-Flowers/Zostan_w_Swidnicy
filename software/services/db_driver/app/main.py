from api import init_api
from database import engine, SessionLocal

app = init_api()

if __name__ == "__main__":
    import uvicorn
    from conf import HOST, PORT
    uvicorn.run(app, host=HOST, port=PORT)
