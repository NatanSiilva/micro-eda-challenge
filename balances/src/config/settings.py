from pydantic import Field
from pydantic_settings import BaseSettings



from pydantic import Field
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    DATABASE_HOST: str = Field(..., env="DATABASE_HOST")
    DATABASE_NAME: str = Field(..., env="DATABASE_NAME")
    DATABASE_PASSWORD: str = Field(..., env="DATABASE_PASSWORD")
    DATABASE_USERNAME: str = Field(..., env="DATABASE_USERNAME")
    KAFKA_INSTANCE: str = Field(..., env="KAFKA_INSTANCE")
    KAFKA_TOPIC_NAME: str = Field(..., env="KAFKA_TOPIC_NAME")

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}/{self.DATABASE_NAME}"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()