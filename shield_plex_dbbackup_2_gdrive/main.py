"""
This module provides the main entry point for handling the backup and restore operations 
for Plex @ Shield database backups to Google Drive.

Functions:
    main(): Main function to handle the backup and restore operations.

Usage:
    Run this module with the appropriate mode to either copy backup files to Google Drive
    or restore them interactively.

Example:
    python main.py --mode copy2gdrive
    python main.py --mode restore
"""

import argparse
import logging
import sys

from shield_plex_dbbackup_2_gdrive.config_context.config_context import \
    ConfigContext
from shield_plex_dbbackup_2_gdrive.modes.copy_to_gdrive import copy_to_gdrive

log_level = ConfigContext().log_level.upper()  # pylint: disable=no-member
logger = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=getattr(logging, log_level, logging.INFO),
    handlers=[
        logging.FileHandler("shield_plex_dbbackup_2_gdrive.log"),
        logging.StreamHandler(sys.stdout),
    ],
)


def main() -> None:
    """
    Main function to handle the backup and restore operations
    for Plex @ Shield database backups to Google Drive.

    The available modes are:
        - "copy2drive": Copies the backup files to Google Drive.
        - "restore": Restores the backup files from Google Drive interactively.

    Raises:
        SystemExit: If an invalid mode is provided.
    """

    logger.info("Starting Shield Plex DB Backup to Google Drive...")

    parser = argparse.ArgumentParser(
        description="Backup Plex @ Shield database backups to Google Drive"
    )

    parser.add_argument(
        "-m",
        "--mode",
        choices=["copy2gdrive", "restore"],
        type=str,
        help=(
            """Application mode: copy2drive for copying the backup files to Google Drive
        or restore for restoring the backup files from Google Drive (interactively)"""
        ),
        required=True,
    )

    arguments = parser.parse_args()

    match arguments.mode:
        case "copy2gdrive":
            copy_to_gdrive()
        # case "restore":
        #     restore()
        case _:
            print("Invalid mode. Exiting...")
            sys.exit(1)


if __name__ == "__main__":
    main()
