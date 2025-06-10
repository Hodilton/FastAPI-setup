# src/app/config.py
from pydantic_settings import BaseSettings
from typing import List
from pathlib import Path
from pydantic import Field

class Settings(BaseSettings):
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str
    DATABASE_URL: str

    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[str] = Field(default_factory=lambda: ["*"])
    PROJECT_NAME: str = "MyApp"

    class Config:
        env_file = str(Path(__file__).resolve().parents[1] / ".env")
        env_file_encoding = 'utf-8'

settings = Settings()