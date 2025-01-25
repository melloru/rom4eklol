from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class DatabaseConfig(BaseModel):
    url: PostgresDsn

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DatabaseConfig


settings = Settings()
