from app.logger import logger
from app.config import CHANNELS
from app.database import Database


def main():

  db = Database()
  db.initialize()

  db.add_channel(
    "channel1",
    "folder1",
    "tokens/channel1.json",
)

  db.close()