from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = 3
ENV_FILE = Path(__file__).resolve().parents[ROOT_DIR] / ".env"


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_database: str
    rabbitmq_default_user: str
    rabbitmq_default_pass: str
    rabbitmq_default_vhost: str
    model_config = SettingsConfigDict(env_file=ENV_FILE, env_file_encoding="utf-8")


settings = Settings()
