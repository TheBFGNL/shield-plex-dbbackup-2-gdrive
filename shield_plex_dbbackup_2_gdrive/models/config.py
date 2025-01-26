"""
This module defines the ConfigContext class for managing configuration settings.

Classes:
    ConfigContext: A Pydantic BaseSettings class for managing configuration settings
                   from environment variables or a .env file.
"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """
    A Pydantic BaseSettings class for managing configuration settings.

    Attributes:
        log_level (str): The logging level for the application.
        smbprotocol_log_level (str): The logging level for the SMB protocol.
        googleapiclient_log_level (str): The logging level for the Google API client.
        shield_host (str): The hostname of the shield.
        shield_user (str): The username for the shield.
        shield_pass (str): The password for the shield.
        shield_share (str): The share name on the shield.
        shield_dbbackup_files_path (str): The path to the backup files on the shield.
        gdrive_root_folder_name (str): The name of the root folder in Google Drive.
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="SHIELDDB2GDRIVE_"
    )

    log_level: str = Field(
        default="INFO", description="The logging level for the application."
    )
    smbprotocol_log_level: str = Field(
        default="WARNING", description="The logging level for the SMB protocol."
    )
    googleapiclient_log_level: str = Field(
        default="WARNING", description="The logging level for the Google API client."
    )
    shield_host: str = Field(description="The hostname of the shield.")
    shield_user: str = Field(description="The username for the shield.")
    shield_pass: str = Field(description="The password for the shield.")
    shield_share: str = Field(description="The share name on the shield.")
    shield_dbbackup_files_path: str = Field(
        description="The path to the backup files on the shield."
    )
    gdrive_root_folder_name: str = Field(
        description="The name of the root folder in Google Drive."
    )
    gdrive_service_account_file: str = Field(
        default="/appl/data/gdrive_service_account.json"
    )
