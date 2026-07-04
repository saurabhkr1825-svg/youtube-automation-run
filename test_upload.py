from app.drive import DriveClient
from app.youtube import YouTubeUploader
from app.config import CHANNELS
from app.metadata.generator import MetadataGenerator

drive = DriveClient()

videos = drive.get_video_files(
    CHANNELS["channel1"]["folder_id"]
)

video = videos[0]

video_path = drive.download_file(
    video["id"],
    video["name"]
)

metadata = MetadataGenerator().generate("channel1")

uploader = YouTubeUploader(
    CHANNELS["channel1"]["token"]
)

video_id = uploader.upload_video(
    video_path=video_path,
    title=metadata["title"],
    description=metadata["description"],
    tags=metadata["tags"],
    privacy="private"
)

print(video_id)