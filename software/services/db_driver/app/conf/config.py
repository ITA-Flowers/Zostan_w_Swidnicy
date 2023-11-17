import os


class Settings:
    def __init__(self, 
                 host       : str = "0.0.0.0", 
                 port       : int = 8080, 
                 db_host    : str = "maria", 
                 db_port    : int = 3306,
                 db_dialect : str = "mysql+pymysql") -> None:
        
        self.host = host
        self.port = port
        
        self.db_host = db_host
        self.db_port = db_port
        self.db_dialect = db_dialect
        
        try:
            self._db_user, self._db_passwd, self._db_name = self.__get_db_env_creds()
        except Exception as why:
            raise RuntimeError(why)
        else:
            self.database_url = f"{self.db_dialect}://{self._db_user}:{self._db_passwd}@{self.db_host}:{self.db_port}/{self._db_name}"
        
    def __get_db_env_creds(self) -> tuple((str, str, str)):
        db_user     = os.getenv('MARIADB_SWIDNICA_USER')
        db_password = os.getenv('MARIADB_SWIDNICA_PASSWORD')
        db_name     = os.getenv('MARIADB_DATABASE')

        if db_user is None or db_password is None or db_name is None:
            raise Exception("Cannot get enviroment variables about DB credentials!")
        else:
            return db_user, db_password, db_name
        
        
        
settings = Settings(host="0.0.0.0", port=8080, db_host="maria", db_port=3306, db_dialect="mysql+pymysql")
