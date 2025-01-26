"""
This module provides functions to interact with an SMB share.

Functions:
    set_smb_connection() -> None:
        Sets up the SMB connection.
    list_smb_files() -> Generator[BackupFile, None, None]:
        Lists files on the SMB share.
    open_smb_file(file: BackupFile) -> BytesIO:
        Opens a file on the SMB share and returns its content as a BytesIO object.
"""

import logging
from io import BytesIO
from typing import Generator

import smbclient
import smbprotocol

from shield_plex_dbbackup_2_gdrive.models.backup_file import BackupFile
from shield_plex_dbbackup_2_gdrive.models.config import Config


config = Config()
logger = logging.getLogger(__name__)
smbprotocol_log_level = config.smbprotocol_log_level

logging.getLogger("smbprotocol").setLevel(
    getattr(logging, config.smbprotocol_log_level, logging.WARNING)
)


def set_smb_connection() -> None:
    """
    Sets up the SMB connection.

    Returns:
        None
    """
    smbclient.register_session(
        server=config.shield_host,
        username=config.shield_user,
        password=config.shield_pass,
        encrypt=True,
    )


def list_smb_files() -> Generator[BackupFile, None, None]:
    # pylint: disable=line-too-long
    """
    Lists files on the SMB share.

    Yields:
        BackupFile: A file on the SMB share.
    """
    # pylint: enable=line-too-long
    set_smb_connection()

    shield_host = config.shield_host
    shield_share = config.shield_share
    smb_dbbackup_files_path = config.shield_dbbackup_files_path

    smb_path = rf"//{shield_host}/{shield_share}/{smb_dbbackup_files_path}"

    try:
        for file in smbclient.scandir(
            smb_path, search_pattern="com.plexapp.plugins.library*.db*"
        ):
            if file.is_file():
                yield BackupFile(file_name=file.name, path=smb_path, file_system="smb")
    except smbprotocol.exceptions.NoSuchFile:
        logger.error("No files found in SMB share '%s'.", smb_path)


def open_smb_file(file: BackupFile) -> BytesIO:
    # pylint: disable=line-too-long
    """
    Opens a file on the SMB share and returns its content as a BytesIO object.

    Args:
        file (BackupFile): The file to be opened.

    Returns:
        BytesIO: The file content as a BytesIO object.
    """
    # pylint: enable=line-too-long
    set_smb_connection()

    shield_host = config.shield_host
    shield_share = config.shield_share
    shield_dbbackup_files_path = config.shield_dbbackup_files_path

    smb_path = rf"//{shield_host}/{shield_share}/{shield_dbbackup_files_path}"

    with smbclient.open_file(rf"{smb_path}/{file.file_name}", mode="rb") as smb_file:
        return BytesIO(smb_file.read())
