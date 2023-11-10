from api import init_api


app = init_api()

if __name__ == "__main__":
    import uvicorn
    from conf import HOST, PORT
    uvicorn.run(app, host=HOST, port=PORT)
