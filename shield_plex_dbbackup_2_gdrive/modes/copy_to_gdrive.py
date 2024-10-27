"""
Module for copying backup files to Google Drive.

This module contains the functionality to copy backup files from a source
to Google Drive using the provided configuration context.

Functions:
    copy_to_gdrive(config_context: ConfigContext) -> None:
"""

import logging
import pathlib

from google.oauth2 import service_account

from shield_plex_dbbackup_2_gdrive.config_context.config_context import \
    ConfigContext
from shield_plex_dbbackup_2_gdrive.handlers import (gdrive_handler,
                                                    shield_handler)

logger = logging.getLogger(__name__)


def copy_to_gdrive(config_context: ConfigContext) -> None:
    """
    Copies backup files to Google Drive.

    This function logs the start of the copying process,
    sets up an SMB connection using the provided configuration context,
    and iterates over the files obtained from the shield handler to copy them
    to Google Drive.

    Args:
        config_context (ConfigContext): The configuration context containing necessary settings
                                        for the operation.

    Returns:
        None
    """
    logger.info("Copying backup files to Google Drive...")

    for file in shield_handler.get_files_at_shield(config_context):
        logger.info("Copying %s to Google Drive...", file.file_name)

    credentials = gdrive_handler.authenticate_with_service_account(config_context)
    print(type(credentials))
