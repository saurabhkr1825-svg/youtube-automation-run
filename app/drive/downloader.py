from pathlib import Path

from googleapiclient.http import MediaIoBaseDownload

from app.config import DOWNLOAD_DIR
from app.logger import logger


class DriveDownloader:

    def __init__(self, service):
        self.service = service

    def download_file(self, file_id: str, filename: str) -> Path:

        DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

        destination = DOWNLOAD_DIR / filename

        request = self.service.files().get_media(fileId=file_id)

        with open(destination, "wb") as file:

            downloader = MediaIoBaseDownload(file, request)

            done = False

            while not done:

                status, done = downloader.next_chunk()

                if status:
                    logger.info(
                        f"Downloading {filename}: {int(status.progress() * 100)}%"
                    )

        logger.info(f"Downloaded: {destination}")

        return destination