from app.drive import DriveClient
from app.config import CHANNELS


def main():

    drive = DriveClient()

    videos = drive.get_video_files(
        CHANNELS["channel1"]["folder_id"]
    )

    print(f"\nFound {len(videos)} videos\n")

    for video in videos[:10]:

        print(video["name"])


if __name__ == "__main__":
    main()