from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="ERF_", extra="ignore")

    service_name: str = "erf"
    log_level: str = "INFO"
