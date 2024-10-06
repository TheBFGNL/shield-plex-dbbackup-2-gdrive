from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


class ConfigContext(BaseSettings):
    load_dotenv()
    model_config = SettingsConfigDict(env_prefix="SHIELDDB2GDRIVE_")

    shield_hostname: str
    shield_share: str
