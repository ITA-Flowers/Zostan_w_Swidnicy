import os


class Settings:
    def __init__(self,
                 host        : str = "0.0.0.0", 
                 port        : int = 8080, 
                 db_drv_host : str = "db_driver",
                 db_drv_port : int = 8080,
                 db_drv_prefix : str = "/api/db_driver") -> None:
        # Server
        self.host = host
        self.port = port
        
        # DB Driver
        self.db_drv_host = db_drv_host
        self.db_drv_port = db_drv_port
        self.db_drv_prefix = db_drv_prefix
        
        # Auth consts
        try:
            self.auth_secret_key, self.auth_algorithm, self.auth_access_token_expires_minutes = self.__get_auth_consts()
        except Exception as why:
            raise RuntimeError(why)
        
    def __get_auth_consts(self) -> tuple((str, str, int)):
        auth_secret_key = os.getenv('AUTH_SECRET_KEY')
        auth_algorithm = os.getenv('AUTH_ALGHORITHM')
        auth_access_token_expires_minutes = os.getenv('AUTH_ACCESS_TOKEN_EXPIRES_MINUTES')
        if auth_secret_key is None or auth_algorithm is None or auth_access_token_expires_minutes is None:
            raise Exception("Cannot get enviroment variables about authentication procedures!")
        else:
            return auth_secret_key, auth_algorithm, int(auth_access_token_expires_minutes)
 
    
settings = Settings()