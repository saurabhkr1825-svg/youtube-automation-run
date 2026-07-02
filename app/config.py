from pathlib import Path

# ===========================
# PROJECT PATHS
# ===========================

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"
LOG_DIR = ROOT_DIR / "logs"
TEMP_DIR = ROOT_DIR / "temp"
DOWNLOAD_DIR = TEMP_DIR / "downloads"

CREDENTIALS_DIR = ROOT_DIR / "credentials"
TOKENS_DIR = ROOT_DIR / "tokens"

# Create folders automatically
for folder in [
    DATA_DIR,
    LOG_DIR,
    TEMP_DIR,
    DOWNLOAD_DIR,
    CREDENTIALS_DIR,
    TOKENS_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)

# ===========================
# DATABASE
# ===========================

DATABASE_PATH = DATA_DIR / "uploads.db"

# ===========================
# GOOGLE DRIVE
# ===========================

SERVICE_ACCOUNT_FILE = CREDENTIALS_DIR / "service_account.json"

# ===========================
# YOUTUBE
# ===========================

YOUTUBE_CLIENT_SECRET = CREDENTIALS_DIR / "youtube_client.json"

# ===========================
# CHANNEL CONFIGURATION
# ===========================

CHANNELS = {

    "channel1": {
        "name": "Channel 1",
        "folder_id": "",
        "token": TOKENS_DIR / "channel1.json",
        "privacy": "public"
    },

    "channel2": {
        "name": "Channel 2",
        "folder_id": "",
        "token": TOKENS_DIR / "channel2.json",
        "privacy": "public"
    },

    "channel3": {
        "name": "Channel 3",
        "folder_id": "",
        "token": TOKENS_DIR / "channel3.json",
        "privacy": "public"
    },

    "channel4": {
        "name": "Channel 4",
        "folder_id": "",
        "token": TOKENS_DIR / "channel4.json",
        "privacy": "public"
    },

    "channel5": {
        "name": "Channel 5",
        "folder_id": "",
        "token": TOKENS_DIR / "channel5.json",
        "privacy": "public"
    },

    "channel6": {
        "name": "Channel 6",
        "folder_id": "",
        "token": TOKENS_DIR / "channel6.json",
        "privacy": "public"
    },

    "channel7": {
        "name": "Channel 7",
        "folder_id": "",
        "token": TOKENS_DIR / "channel7.json",
        "privacy": "public"
    },

    "channel8": {
        "name": "Channel 8",
        "folder_id": "",
        "token": TOKENS_DIR / "channel8.json",
        "privacy": "public"
    }

}