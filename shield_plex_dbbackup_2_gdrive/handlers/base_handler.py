"""
This module provides a function to identify files that are present on the shield but not on Google Drive.

Functions:
    not_on_gdrive(shield_file_list: list[BackupFile], gdrive_file_list: list[BackupFile]) -> Generator[BackupFile, None, None]:
        Returns a generator of files that are not on Google Drive.
"""

from typing import Generator
from shield_plex_dbbackup_2_gdrive.classes.backup_file import BackupFile

def not_on_gdrive(
    shield_file_list: list[BackupFile], gdrive_file_list: list[BackupFile]
) -> Generator[BackupFile, None, None]:
    """
    Returns a generator of files that are not on Google Drive.

    This function takes a list of files on the shield and a list of files on Google Drive
    and returns a generator of files that are not on Google Drive.

    Args:
        shield_file_list (list[BackupFile]): The list of files on the shield.
        gdrive_file_list (list[BackupFile]): The list of files on Google Drive.

    Yields:
        BackupFile: A file that is on the shield but not on Google Drive.
    """
    yield from (file for file in shield_file_list if file not in gdrive_file_list)
