from pathlib import Path

from google.auth.transport.requests import Request # pyright: ignore[reportMissingImports]
from google.oauth2.credentials import Credentials # pyright: ignore[reportMissingImports]
from google_auth_oauthlib.flow import InstalledAppFlow # pyright: ignore[reportMissingImports]

from app.config import YOUTUBE_CLIENT_SECRET

# YouTube Upload Scope
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload"
]


class YouTubeAuth:

    def __init__(self, token_path: Path):
        self.token_path = Path(token_path)

    def authenticate(self) -> Credentials:

        credentials = None

        # --------------------------
        # Load Existing Token
        # --------------------------

        if self.token_path.exists():
            credentials = Credentials.from_authorized_user_file(
                str(self.token_path),
                SCOPES
            )

        # --------------------------
        # Refresh Token
        # --------------------------

        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

        # --------------------------
        # First Login
        # --------------------------

        elif not credentials or not credentials.valid:

            flow = InstalledAppFlow.from_client_secrets_file(
                str(YOUTUBE_CLIENT_SECRET),
                SCOPES
            )

            credentials = flow.run_local_server(port=0)

            self.token_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(self.token_path, "w") as token:
                token.write(credentials.to_json())

        return credentials