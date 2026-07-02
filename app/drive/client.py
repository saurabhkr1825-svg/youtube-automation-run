from .auth import authenticate_drive


class DriveClient:

    def __init__(self):
        self.service = authenticate_drive()

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

        videos = []

        for file in files:

            if file["mimeType"].startswith("video/"):

                videos.append(file)

        return videos