from google.oauth2 import service_account
from googleapiclient.discovery import build

from shield_plex_dbbackup_2_gdrive.config_context.config_context import \
    ConfigContext


def authenticate_with_service_account(
    config_context: ConfigContext,
) -> service_account.Credentials:

    credentials = service_account.Credentials.from_service_account_file(
        config_context.gdrive_service_account_file,
        scopes=["https://www.googleapis.com/auth/drive"],
    )

    build_service(credentials)


    return credentials

def build_service(credentials: service_account.Credentials) -> None:
    


  try:
    service = build("drive", "v3", credentials=credentials)

    # Call the Drive v3 API
    results = (
        service.files()
        .list(pageSize=10, fields="nextPageToken, files(id, name)")
        .execute()
    )
    items = results.get("files", [])

    if not items:
      print("No files found.")
      return
    print("Files:")
    for item in items:
      print(f"{item['name']} ({item['id']})")
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")
