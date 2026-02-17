from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Rydum Backend"
    API_V1_STR: str = "/api/v1"
    
    # Add any other core settings here (e.g., database URL, debug mode)
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
