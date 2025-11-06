from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parent.parent / ".env"

class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_database: str
    rabbitmq_default_user: str
    rabbitmq_default_pass: str
    rabbitmq_default_vhost: str
    rabbitmq_host: str
    insight_message_queue: str
    document_bucket: str
    minio_root_user: str
    minio_root_password: str
    minio_endpoint: str
    model_config = SettingsConfigDict(env_file=ENV_FILE, env_file_encoding="utf-8")


settings = Settings()
