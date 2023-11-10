import os

# Server
HOST : str = "0.0.0.0"
PORT : int = 8080

# Database
DATABASE_HOST = "maria"
DATABASE_PORT = 9050

def get_db_creds() -> tuple((str, str, str)):
    db_user     = os.getenv('MARIADB_USER')
    db_password = os.getenv('MARIADB_PASSWORD')
    db_name     = os.getenv('MARIADB_DATABASE')
    
    if db_user is None or db_password is None or db_name is None:
        raise Exception("Cannot get enviroment variables about DB credentials!")
    else:
        return db_user, db_password, db_name

try:
    DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME = get_db_creds()
except Exception as why:
    raise RuntimeError(str(why))
else:
    DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    print(DATABASE_URL)
    