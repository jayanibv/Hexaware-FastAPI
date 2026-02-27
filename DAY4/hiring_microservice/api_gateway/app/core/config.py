from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # Service URLs
    AUTH_SERVICE_URL: str = "http://auth-service:8001"
    USER_SERVICE_URL: str = "http://user-service:8002"
    COMPANY_SERVICE_URL: str = "http://company-service:8003"
    JOB_SERVICE_URL: str = "http://job-service:8005"
    APPLICATION_SERVICE_URL: str = "http://application-service:8004"

    # Gateway settings
    SECRET_KEY: Optional[str] = None
    ALGORITHM: Optional[str] = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = 60

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        extra="ignore"
    )
    
settings = Settings()