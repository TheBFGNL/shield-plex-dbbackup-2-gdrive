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

def get_root_folder_id() -> str:
    
        service = authenticate_with_service_account()

        root_folder_name = ConfigContext().gdrive_root_folder_name
        fields = "files(id)"

        results = service.files().list(q=f"name='{root_folder_name}'", fields=fields).execute()  # pylint: disable=no-member
        root_folder_id = results.get("files", [])

        print(f"RootFolderID: {root_folder_id}")



def list_gdrive_files() -> None:

    get_root_folder_id()
    service = authenticate_with_service_account()
    fields = "files(id)"

    results = service.files().list(fields=fields).execute()  # pylint: disable=no-member
    files = results.get("files", [])

    for file in files:
        yield file
