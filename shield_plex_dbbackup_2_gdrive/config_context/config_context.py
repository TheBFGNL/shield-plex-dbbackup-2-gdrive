"""
config_context.py

This module defines the `ConfigContext` class, which is used to manage configuration settings 
for the Shield Plex DB Backup to Google Drive application. The configuration settings are 
loaded from environment variables, with support for reading from a `.env` file.

Classes:
    ConfigContext: A Pydantic BaseSettings subclass that defines the configuration settings 
                   for the application.

Attributes:
    model_config (SettingsConfigDict): Configuration for loading settings from environment 
                                       variables and `.env` file.
    shield_host (str): The host address for the Shield service.
    shield_user (str): The username for the Shield service.
    shield_pass (str): The password for the Shield service.
    shield_share (str): The share name for the Shield service.
    shield_dbbackup_files_path (str): The file path for Shield database backup files.
"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigContext(BaseSettings):
    """
    Configuration context for the Shield Plex DB Backup to Google Drive application.

    This class uses Pydantic's BaseSettings to load configuration from environment variables
    defined in a .env file. The environment variables are prefixed with 'SHIELDDB2GDRIVE_'.

    Attributes:
        shield_host (str): The host address of the Shield server.
        shield_user (str): The username for accessing the Shield server.
        shield_pass (str): The password for accessing the Shield server.
        shield_share (str): The shared directory on the Shield server.
        shield_dbbackup_files_path (str): The file path for Shield database backups.
        logging_level (str): The logging level for the application. Default is 'INFO'.
        smb_logging_level (str): The logging level for the SMB client. Default is 'WARNING'.
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="SHIELDDB2GDRIVE_"
    )

    logging_level: str = Field(default="INFO")
    smb_logging_level: str = Field(default="WARNING")
    shield_host: str = Field()
    shield_user: str = Field()
    shield_pass: str = Field()
    shield_share: str = Field()
    shield_dbbackup_files_path: str = Field()
    gdrive_service_account_file: str = Field(
        default="/appl/data/gdrive_service_account.json"
    )
