import logging

from google.oauth2 import service_account
from googleapiclient.discovery import Resource, build

from shield_plex_dbbackup_2_gdrive.classes.backup_file import BackupFile
from shield_plex_dbbackup_2_gdrive.config_context.config_context import \
    ConfigContext


def authenticate_with_service_account() -> Resource:

    credentials = service_account.Credentials.from_service_account_file(
        ConfigContext().gdrive_service_account_file,
        scopes=["https://www.googleapis.com/auth/drive"],
    )

    service = build_service(credentials)

    return service


def build_service(credentials: service_account.Credentials) -> Resource:

    service = build("drive", "v3", credentials=credentials)
    print(type(service))

    return service


def list_gdrive_files() -> None:

    service = authenticate_with_service_account()
    fields = "files(id)"

    results = service.files().list(fields=fields).execute()  # pylint: disable=no-member
    files = results.get("files", [])

    for file in files:
        yield file
