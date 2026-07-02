from google.oauth2 import service_account
from googleapiclient.discovery import build

from app.config import SERVICE_ACCOUNT_FILE


SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly"
]


def authenticate_drive():

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
    )

    return build(
        "drive",
        "v3",
        credentials=credentials,
    )