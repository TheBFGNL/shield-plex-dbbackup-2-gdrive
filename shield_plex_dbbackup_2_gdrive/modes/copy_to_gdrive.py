import logging
import os
import shutil

import smbclient

from shield_plex_dbbackup_2_gdrive.config_context import ConfigContext

logger = logging.getLogger(__name__)


def copy_to_gdrive(config_context: ConfigContext) -> None:
    logger.info("Copying backup files to Google Drive...")

    shield_host = config_context.shield_host
    shield_share = config_context.shield_share

    # Get files from Shield samba share

    return None
