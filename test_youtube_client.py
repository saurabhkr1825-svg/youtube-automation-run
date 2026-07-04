from app.youtube import YouTubeClient
from app.config import CHANNELS


youtube = YouTubeClient(
    CHANNELS["channel1"]["token"]
)

service = youtube.get_service()

channel = (
    service.channels()
    .list(
        part="snippet",
        mine=True
    )
    .execute()
)

print(channel["items"][0]["snippet"]["title"])