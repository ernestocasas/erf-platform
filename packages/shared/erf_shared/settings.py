from pydantic_settings import BaseSettings, SettingsConfigDict


class ERFSettings(BaseSettings):
    """Base settings shared by all ERF services.

    Environment variables are prefixed with `ERF_`.
    """

    model_config = SettingsConfigDict(env_prefix="ERF_", case_sensitive=False)

    service_name: str = "erf_service"
    log_level: str = "INFO"
    version: str = "0.1.0"


def get_settings() -> ERFSettings:
    # Simple singleton-ish instance; in real code you'd cache via lru_cache.
    return ERFSettings()
