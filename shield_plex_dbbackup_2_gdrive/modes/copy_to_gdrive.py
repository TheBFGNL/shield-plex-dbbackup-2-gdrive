"""
Module for copying backup files to Google Drive.
This module contains the function to copy backup files from an SMB share to Google Drive.
Functions:
    copy_to_gdrive: Copies backup files from an SMB share to Google Drive.
"""

import logging

from shield_plex_dbbackup_2_gdrive.classes.backup_file import BackupFile
from shield_plex_dbbackup_2_gdrive.handlers import (base_handler,
                                                    gdrive_handler,
                                                    smb_handler)

logger = logging.getLogger(__name__)


def copy_to_gdrive() -> None:
    """
    Copies backup files from an SMB share to Google Drive.
    This function performs the following steps:
    1. Retrieves the list of files from the SMB share and logs the filenames.
    2. Retrieves the list of files from Google Drive.
    3. Identifies files that are present on the SMB share but not on Google Drive.
    4. Copies the missing files from the SMB share to Google Drive.
    Returns:
        None
    """

    shield_file_list: list[BackupFile] = []
    gdrive_file_list: list[BackupFile] = []

    logger.info("Copying backup files to Google Drive...")
    logger.info("Getting files on the smb share of the shield")

    for file in smb_handler.list_smb_files():
        shield_file_list.append(file)
        logger.debug("Found file: %s", file.file_name)

    logger.info("Found %s files on the smb share", len(shield_file_list))

    logger.info("Getting files on Google Drive")
    for file in gdrive_handler.list_gdrive_files():
        gdrive_file_list.append(file)
    logger.info("Found %s files on Google Drive", len(gdrive_file_list))

    for file in base_handler.not_on_gdrive(shield_file_list, gdrive_file_list):
        logger.info("%s is not found on Google Drive.", file.file_name)
        logger.info("Copying %s to Google Drive...", file.file_name)

        io_bytes = smb_handler.open_smb_file(file)

        gdrive_handler.upload_file(file, io_bytes)
