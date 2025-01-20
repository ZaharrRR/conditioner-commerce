from pathlib import Path
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# корневая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class ConfigBase(BaseSettings):
    """Базовые настройки конфига"""

    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env", env_file_encoding="utf-8", extra="ignore"
    )


class ApiConfig(ConfigBase):
    host: str
    port: int

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


class RedisConfig(ConfigBase):
    host: str
    port: int
    password: str
    database: int

    model_config = SettingsConfigDict(env_prefix="redis_")


class Settings(BaseSettings):
    """Глобальные настройки"""

    api: ApiConfig = Field(default_factory=ApiConfig)
    telegram: TelegramConfig = Field(default_factory=TelegramConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    redis: RedisConfig = Field(default_factory=RedisConfig)

    def get_db_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.database.user}:"
            f"{self.database.password}@{self.database.host}:"
            f"{self.database.port}/{self.database.db}"
        )


settings = Settings()
