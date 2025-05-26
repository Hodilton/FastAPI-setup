# src/app/config.py
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str
    DATABASE_URL: str
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "supersecretkey123"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 11520
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    PROJECT_NAME: str = "My FastAPI App"

    class Config:
        env_file = "./.env"

settings = Settings()
