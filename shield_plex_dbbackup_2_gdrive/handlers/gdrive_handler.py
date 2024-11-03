import logging
import sys
from io import BytesIO
from typing import Generator

from google.oauth2 import service_account
from googleapiclient.discovery import Resource, build
from googleapiclient.http import MediaIoBaseUpload

from shield_plex_dbbackup_2_gdrive.classes.backup_file import BackupFile
from shield_plex_dbbackup_2_gdrive.config_context.config_context import \
    ConfigContext

googleapiclient_log_level = ConfigContext().googleapiclient_log_level

logging.getLogger("googleapiclient").setLevel(
    getattr(logging, googleapiclient_log_level, logging.WARNING)
)


def authenticate_with_service_account() -> service_account.Credentials:

    credentials = service_account.Credentials.from_service_account_file(
        ConfigContext().gdrive_service_account_file,
        scopes=["https://www.googleapis.com/auth/drive"],
    )

    return credentials


def build_service() -> Resource:

    credentials = authenticate_with_service_account()
    service = build("drive", "v3", credentials=credentials)

    return service


def get_root_folder_id() -> str:

    service = build_service()

    root_folder_name = ConfigContext().gdrive_root_folder_name
    fields = "files(id)"

    # pylint: disable=no-member
    root_folder_id = (
        service.files()
        .list(q=f"name='{root_folder_name}'", fields=fields)
        .execute()
        .get("files", [])
    )
    # pylint: enable=no-member

    if not root_folder_id:
        logging.error("Root folder '%s' not found in Google Drive.", root_folder_name)
        sys.exit(1)
    elif len(root_folder_id) > 1:
        logging.error(
            "Multiple root folders with name '%s' found in Google Drive.",
            root_folder_name,
        )
        sys.exit(1)
    else:
        root_folder_id = root_folder_id[0]["id"]

    return root_folder_id


def list_gdrive_files() -> Generator[BackupFile, None, None]:

    root_folder_id = get_root_folder_id()

    service = build_service()
    fields = "files(name, id)"
    q = f"parents='{root_folder_id}' and name contains 'com.plexapp.plugins.library'"

    # pylint: disable=no-member
    files = service.files().list(fields=fields, q=q).execute().get("files", [])
    # pylint: enable=no-member

    for file in files:
        yield BackupFile(
            file_name=file["name"], path=root_folder_id, file_system="gdrive"
        )


def upload_file(file: BackupFile, io_bytes: BytesIO) -> None:

    root_folder_id = get_root_folder_id()
    service = build_service()

    file_metadata = {
        "name": file.file_name,
        "parents": [root_folder_id],
    }

    media = MediaIoBaseUpload(
        io_bytes, mimetype="application/octet-stream", resumable=True
    )

    # pylint: disable=no-member
    service.files().create(body=file_metadata, media_body=media).execute()
    # pylint: enable=no-member
