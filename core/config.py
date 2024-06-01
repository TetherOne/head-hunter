from dotenv import load_dotenv
from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    resumes: str = "/resumes"
    contacts: str = "/contacts"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FAST_API_HH__",
    )
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
