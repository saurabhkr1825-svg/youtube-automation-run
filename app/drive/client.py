from .auth import authenticate_drive
from .downloader import DriveDownloader


class DriveClient:

    def __init__(self):

        self.service = authenticate_drive()

        self.downloader = DriveDownloader(self.service)

    def list_files(self, folder_id):

        results = (
            self.service.files()
            .list(
                q=f"'{folder_id}' in parents and trashed=false",
                fields="files(id,name,mimeType,createdTime)"
            )
            .execute()
        )

        return results.get("files", [])

    def get_video_files(self, folder_id):

        files = self.list_files(folder_id)

        return [
            file
            for file in files
            if file["mimeType"].startswith("video/")
        ]

    def download_file(self, file_id, filename):

        return self.downloader.download_file(
            file_id,
            filename
        )