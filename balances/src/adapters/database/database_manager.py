from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine
from src.config.settings import settings

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseManager(metaclass=MetaSingleton):
    def __init__(self) -> None:
        self.settings = settings
        self.engine = self.connect(self.settings.DATABASE_URL)
        
    @staticmethod
    def connect(database_url: str):
        return create_engine(database_url)
    
    def get_session(self) -> Session:
        return Session(bind=self.engine)

