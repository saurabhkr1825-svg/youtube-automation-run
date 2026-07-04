from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from app.config import SERVICE_ACCOUNT_FILE


class Database:

    def __init__(self):

        if not firebase_admin._apps:
            cred = credentials.Certificate(
                SERVICE_ACCOUNT_FILE
            )
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def initialize(self):
        pass

    def is_uploaded(self, channel, drive_file_id):

        doc = (
            self.db.collection("uploads")
            .document(f"{channel}_{drive_file_id}")
            .get()
        )

        return doc.exists

    def add_upload(
        self,
        channel,
        filename,
        drive_file_id,
        youtube_video_id,
        title
    ):

        self.db.collection("uploads").document(
            f"{channel}_{drive_file_id}"
        ).set({

            "channel": channel,
            "filename": filename,
            "drive_file_id": drive_file_id,
            "youtube_video_id": youtube_video_id,
            "title": title,
            "uploaded_at": datetime.utcnow()

        })