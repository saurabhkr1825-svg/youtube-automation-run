from app.drive import DriveClient
from app.youtube import YouTubeUploader
from app.database import Database
from app.metadata.generator import MetadataGenerator
from app.config import CHANNELS


class UploadPipeline:

    def __init__(self):

        self.drive = DriveClient()

        self.db = Database()

        self.db.initialize()

        self.generator = MetadataGenerator()

    def run(self):

        for channel, config in CHANNELS.items():
            try:
                print(f"\n===== {channel} =====")

                videos = self.drive.get_video_files(
                    config["folder_id"]
                )

                for video in videos:

                    if self.db.is_uploaded(
                        channel,
                        video["id"]
                    ):
                        continue

                    metadata = self.generator.generate(channel)

                    video_path = self.drive.download_file(
                        video["id"],
                        video["name"]
                    )

                    uploader = YouTubeUploader(
                        config["token"]
                    )

                    video_id = uploader.upload_video(
                        video_path=video_path,
                        title=metadata["title"],
                        description=metadata["description"],
                        tags=metadata["tags"],
                        privacy=config["privacy"]
                    )

                    self.db.add_upload(
                        channel=channel,
                        filename=video["name"],
                        drive_file_id=video["id"],
                        youtube_video_id=video_id,
                        title=metadata["title"]
                    )
                    
                    video_path.unlink()

                    print(f"✅ Uploaded {video['name']}")

                    break   # Upload only one video for this channel

            except Exception as e:
                print(f"❌ {channel} failed: {e}")
                continue