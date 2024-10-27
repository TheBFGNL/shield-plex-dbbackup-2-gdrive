import logging
import os
from typing import Generator

import smbclient

from shield_plex_dbbackup_2_gdrive.classes.backup_file import BackupFile
from shield_plex_dbbackup_2_gdrive.config_context.config_context import \
    ConfigContext

logger = logging.getLogger(__name__)
logging.getLogger("smbprotocol").setLevel(logging.WARNING)


def set_smb_connection(config_context: ConfigContext) -> None:

    smbclient.register_session(
        server=config_context.shield_host,
        username=config_context.shield_user,
        password=config_context.shield_pass,
        encrypt=True,
    )

    return None


def get_files_at_shield(config_context: ConfigContext) -> Generator[BackupFile, None, None]:  # type: ignore[return]

    set_smb_connection(config_context)

    smb_path = rf"//{config_context.shield_host}/{config_context.shield_share}/{config_context.shield_dbbackup_files_path}"

    file_list = smbclient.listdir(smb_path)

    for file in file_list:
        yield BackupFile(file_name=file, path=smb_path, file_system="smb")
