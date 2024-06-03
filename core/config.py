from fastapi import Path
from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    resumes: str = "/resumes"
    contacts: str = "/contacts"
    vacancies: str = "/vacancies"
    auth: str = "/auth"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class S3Config(BaseModel):
    access_key: str
    secret_key: str
    endpoint_url: str
    bucket_name: str


class AuthJWT(BaseModel):
    private_key_path: Path = "env/jwt-private.pem"
    public_key_path: Path = "env/jwt-public.pem"
    algorithm: str = "RS256"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="env/.env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FAST_API_HH__",
    )
    api: ApiPrefix = ApiPrefix()
    s3: S3Config
    db: DatabaseConfig
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
