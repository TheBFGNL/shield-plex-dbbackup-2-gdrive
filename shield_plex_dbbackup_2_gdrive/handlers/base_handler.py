from typing import Generator

from shield_plex_dbbackup_2_gdrive.classes.backup_file import BackupFile


def not_on_gdrive(
    shield_file_list: list[BackupFile], gdrive_file_list: list[BackupFile]
) -> Generator[BackupFile, None, None]:
    """
    Returns a list of files that are not on Google Drive.

    This function takes a list of files on the shield and a list of files on Google Drive
    and returns a list of files that are not on Google Drive.

    Args:
        shield_file_list (list): The list of files on the shield.
        gdrive_file_list (list): The list of files on Google Drive.

    Returns:
        list: The list of files that are not on Google Drive.
    """

    yield from (file for file in shield_file_list if file not in gdrive_file_list)
