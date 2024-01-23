import os


class Settings:
    def __init__(self,
                 host        : str = "0.0.0.0") -> None:
        # Server
        self.host = host
        self.port = int(os.getenv("AUTH_PORT_IN", "8080"))

    
settings = Settings()