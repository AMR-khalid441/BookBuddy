from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    APP_NAME:str
    APP_VERSION:str
    OPENAI_API_KEY:str
    FILE_MAX_SIZE:int
    FILE_ALLOWED_TYPES:list
    FILE_CHUNK_SIZE:int

    class Config :
        env_file =".env"

def get_settings():
    return Settings()