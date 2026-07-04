from app.drive import DriveClient
from app.config import CHANNELS


def main():

    drive = DriveClient()

    videos = drive.get_video_files(
        CHANNELS["channel1"]["folder_id"]
    )

    if not videos:
        print("No videos found.")
        return

    video = videos[0]

    print(video["name"])

    path = drive.download_file(
        video["id"],
        video["name"]
    )

    print(path)


if __name__ == "__main__":
    main()