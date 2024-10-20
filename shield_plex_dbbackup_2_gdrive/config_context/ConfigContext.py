from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigContext(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="SHIELDDB2GDRIVE_"
    )

    shield_host: str
    shield_share: str
