from app.database.firestore_database import FirestoreDatabase

db = FirestoreDatabase()

print("Already uploaded:", db.is_uploaded("channel1", "abc123"))

db.add_upload(
    channel="channel1",
    filename="test.mp4",
    drive_file_id="abc123",
    youtube_video_id="youtube123",
    title="Test Video",
)

print("Already uploaded:", db.is_uploaded("channel1", "abc123"))