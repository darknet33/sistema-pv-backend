from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    JWT_SECRET: str = "super-secret-key-change-in-production-2026"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SESSION_IDLE_TIMEOUT_MINUTES: int | None = None

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def idle_timeout_minutes(self) -> int:
        return self.SESSION_IDLE_TIMEOUT_MINUTES or self.ACCESS_TOKEN_EXPIRE_MINUTES


settings = Settings()
