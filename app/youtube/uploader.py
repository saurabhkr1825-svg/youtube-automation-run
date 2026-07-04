from pathlib import Path

from googleapiclient.http import MediaFileUpload

from app.logger import logger

from .client import YouTubeClient


class YouTubeUploader:

    def __init__(self, token_path):

        self.client = YouTubeClient(token_path)

        self.service = self.client.get_service()

    def upload_video(
        self,
        video_path: Path,
        title: str,
        description: str,
        tags: list[str],
        privacy: str = "public",
        category: str = "22",
        made_for_kids: bool = False,
    ):

        body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": category,
            },
            "status": {
                "privacyStatus": privacy,
                "selfDeclaredMadeForKids": made_for_kids,
            },
        }

        media = MediaFileUpload(
            str(video_path),
            chunksize=-1,
            resumable=True,
        )

        request = self.service.videos().insert(
            part="snippet,status",
            body=body,
            media_body=media,
        )

        logger.info(f"Uploading {video_path.name}...")

        response = None

        while response is None:

            status, response = request.next_chunk()

            if status:
                logger.info(
                    f"Upload Progress: {int(status.progress() * 100)}%"
                )

        video_id = response["id"]

        logger.info(f"Upload Complete!")

        logger.info(f"Video ID: {video_id}")

        return video_id