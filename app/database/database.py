import sqlite3

from app.config import DATABASE_PATH
from app.logger import logger


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def initialize(self):
        self.create_tables()
    
    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS channels (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT UNIQUE NOT NULL,

            folder_id TEXT NOT NULL,

            token_path TEXT NOT NULL,

            privacy TEXT DEFAULT 'public',

            total_uploads INTEGER DEFAULT 0,

            last_upload TEXT
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS uploads (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            channel TEXT NOT NULL,

            filename TEXT NOT NULL,

            drive_file_id TEXT,

            youtube_video_id TEXT,

            title TEXT,

            status TEXT DEFAULT 'PENDING',

            uploaded INTEGER DEFAULT 0,

            upload_date TEXT,

            UNIQUE(channel, filename)
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            channel TEXT,

            filename TEXT,

            level TEXT,

            message TEXT,

            created_at TEXT
        );
        """)

        self.connection.commit()

        logger.info("Database tables created successfully.")
    

    def is_uploaded(self, channel: str, drive_file_id: str) -> bool:
        self.cursor.execute(
            """
            SELECT 1
            FROM uploads
            WHERE channel = ?
            AND drive_file_id = ?
            """,
            (
                channel,
                drive_file_id
            ),
        )

        return self.cursor.fetchone() is not None

    def add_channel(
        self,
        name: str,
        folder_id: str,
        token_path: str,
        privacy: str = "public",
    ):
        self.cursor.execute(
            """
            INSERT OR IGNORE INTO channels
            (name, folder_id, token_path, privacy)
            VALUES (?, ?, ?, ?)
            """,
            (name, folder_id, token_path, privacy),
        )

        self.connection.commit()

        logger.info(f"Channel '{name}' registered.")

    def get_channel(self, name: str):
        self.cursor.execute(
            """
            SELECT *
            FROM channels
            WHERE name = ?
            """,
            (name,),
        )

        return self.cursor.fetchone()

    def add_upload(
        self,
        channel: str,
        filename: str,
        drive_file_id: str,
        youtube_video_id: str,
        title: str,
        status: str = "PENDING",
    ):
        self.cursor.execute(
            """
            INSERT OR IGNORE INTO uploads
            (
                channel,
                filename,
                drive_file_id,
                youtube_video_id,
                title,
                status,
                uploaded,
                upload_date
            )
            VALUES (?, ?, ?, ?, ?, ?, 1, datetime('now'))
            """,
            (
                channel,
                filename,
                drive_file_id,
                youtube_video_id,
                title,
                status,
            ),
        )

        self.connection.commit()

    def close(self):
        self.connection.close()
    