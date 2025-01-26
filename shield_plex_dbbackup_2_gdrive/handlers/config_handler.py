"""
This module provides a handler for loading configuration settings.

Functions:
    load: Load the configuration settings from environment variables or a .env file.
"""

import sys

from pydantic import ValidationError

from shield_plex_dbbackup_2_gdrive.models.config import Config


def load() -> Config:
    """
    Load the configuration settings from environment variables or a .env file.

    Returns:
        Config: The configuration settings.

    Raises:
        SystemExit: If there is an error loading the configuration.
    """
    try:
        config = Config()
        return config
    except ValidationError as error:
        print(f"Error loading configuration: \n {error}")
        sys.exit(1)
