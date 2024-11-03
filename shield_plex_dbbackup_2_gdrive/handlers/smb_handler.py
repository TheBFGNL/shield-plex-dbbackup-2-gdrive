import logging
from io import BytesIO
from typing import Generator

import smbclient
import smbprotocol

from shield_plex_dbbackup_2_gdrive.classes.backup_file import BackupFile
from shield_plex_dbbackup_2_gdrive.config_context.config_context import \
    ConfigContext

logger = logging.getLogger(__name__)
smbprotocol_log_level = ConfigContext().smbprotocol_log_level

logging.getLogger("smbprotocol").setLevel(
    getattr(logging, ConfigContext().smbprotocol_log_level, logging.WARNING)
)


def set_smb_connection() -> None:

    smbclient.register_session(
        server=ConfigContext().shield_host,
        username=ConfigContext().shield_user,
        password=ConfigContext().shield_pass,
        encrypt=True,
    )

    return None


def list_smb_files() -> Generator[BackupFile, None, None]:

    set_smb_connection()

    smb_path = rf"//{ConfigContext().shield_host}/{ConfigContext().shield_share}/{ConfigContext().shield_dbbackup_files_path}"

    try:
        for file in smbclient.scandir(
            smb_path, search_pattern="com.plexapp.plugins.library*.db*"
        ):
            if file.is_file():

                yield BackupFile(file_name=file.name, path=smb_path, file_system="smb")
    except smbprotocol.exceptions.NoSuchFile:
        logger.error("No files found in SMB share '%s'.", smb_path)


def open_smb_file(file: BackupFile) -> BytesIO:

    set_smb_connection()

    smb_path = rf"//{ConfigContext().shield_host}/{ConfigContext().shield_share}/{ConfigContext().shield_dbbackup_files_path}"

    with smbclient.open_file(rf"{smb_path}/{file.file_name}", mode="rb") as smb_file:
        return BytesIO(smb_file.read())
