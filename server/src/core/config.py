import os
from pathlib import Path
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# корневая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
print(BASE_DIR)
env_file=BASE_DIR / ".env"

class ConfigBase(BaseSettings):
    """Базовые настройки конфига"""

    model_config = SettingsConfigDict(
        env_file=f"{env_file}", env_file_encoding="utf-8", extra="ignore"
    )


class ApiConfig(ConfigBase):
    host: str
    port: int
    admin_key: str
    model_config = SettingsConfigDict(env_prefix="api_")


class TelegramConfig(ConfigBase):
    bot_token: str
    admin_ids: List[int]

    model_config = SettingsConfigDict(env_prefix="tg_")


class DatabaseConfig(ConfigBase):
    user: str
    password: str
    db: str
    host: str
    port: int

    model_config = SettingsConfigDict(env_prefix="postgres_")


class S3Config(ConfigBase):
    access_key: str
    secret_key: str
    bucket_name: str
    endpoint: str
    region: str
    account_id: str

    model_config = SettingsConfigDict(env_prefix="s3_", extra="ignore")


class Settings(BaseSettings):
    """Глобальные настройки"""

    api: ApiConfig = Field(default_factory=ApiConfig)
    telegram: TelegramConfig = Field(default_factory=TelegramConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    s3: S3Config = Field(default_factory=S3Config)

    def get_db_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.database.user}:"
            f"{self.database.password}@{self.database.host}:"
            f"{self.database.port}/{self.database.db}"
        )


settings = Settings()
