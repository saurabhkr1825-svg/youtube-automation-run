from dataclasses import dataclass
from datetime import datetime


@dataclass
class UploadRecord:
    channel: str
    filename: str
    drive_file_id: str = ""
    youtube_video_id: str = ""
    title: str = ""
    uploaded: bool = False
    upload_date: str = datetime.now().isoformat()
    status: str = "PENDING"