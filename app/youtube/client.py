from googleapiclient.discovery import build

from .auth import YouTubeAuth


class YouTubeClient:

    def __init__(self, token_path):

        auth = YouTubeAuth(token_path)

        credentials = auth.authenticate()

        self.service = build(
            "youtube",
            "v3",
            credentials=credentials
        )

    def get_service(self):

        return self.service