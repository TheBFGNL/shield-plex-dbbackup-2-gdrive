"""
Module for copying backup files to Google Drive.

This module contains the functionality to copy backup files from a source
to Google Drive using the provided configuration context.

Functions:
    copy_to_gdrive(config_context: ConfigContext) -> None:
"""

import logging

from shield_plex_dbbackup_2_gdrive.classes.backup_file import BackupFile
from shield_plex_dbbackup_2_gdrive.config_context.config_context import \
    ConfigContext
from shield_plex_dbbackup_2_gdrive.handlers import gdrive_handler, smb_handler

logger = logging.getLogger(__name__)


def copy_to_gdrive() -> None:
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

    shield_file_list: list = []
    gdrive_file_list: list = []
    not_on_gdrive_file_list: list = []

    logger.info("Copying backup files to Google Drive...")
    logger.info("Getting files on the smb share of the shield")

    for file in smb_handler.list_smb_files():
        shield_file_list.append(file)
        logger.debug(f"Found file: {file.file_name}")

    logger.info("Found %s files on the smb share", len(shield_file_list))

    logger.info("Getting files on Google Drive")
    for file in gdrive_handler.list_gdrive_files():
        gdrive_file_list.append(file)

        print(file)
