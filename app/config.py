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
        "folder_id": "1EYh2ciXrClaa6VqvTugT0svN65ioQwuP",
        "uploaded_folder_id": "10_Rn4SEpil-3xNP-r5g2GnkYF5KFVM2c",
        "token": TOKENS_DIR / "channel1.json",
        "privacy": "public"
    },

    "channel2": {
        "name": "Channel 2",
        "folder_id": "1fHocToV-tG3wnJw97lY-AyiPeYv9zc41",
        "uploaded_folder_id": "1bxEEymVPOEcQjsn1yMc7AfD1kEq5sTxF",
        "token": TOKENS_DIR / "channel2.json",
        "privacy": "public"
    },

    "channel3": {
        "name": "Channel 3",
        "folder_id": "1-ZmLAA8jny3NgdcQhRziebTUZERilVV1",
        "uploaded_folder_id": "1sYzvl2c1TnJHwFzq5hzGLnQWxwW60la8",
        "token": TOKENS_DIR / "channel3.json",
        "privacy": "public"
    },

    "channel4": {
        "name": "Channel 4",
        "folder_id": "1cEjHNHOOTet7NmhzOKP2OxA9Ca9sBwru",
        "uploaded_folder_id": "17dlTLoFLg_mT7HFcV8mAH_9eSCrDn2WG",
        "token": TOKENS_DIR / "channel4.json",
        "privacy": "public"
    },

    "channel5": {
        "name": "Channel 5",
        "folder_id": "1vuqz9RXbIU6puItX1xPAjx8svAWrR7Zw",
        "uploaded_folder_id": "140A0ogBua3Xe4dfq5KeBkjZJtqdKLKX7",
        "token": TOKENS_DIR / "channel5.json",
        "privacy": "public"
    },

    "channel6": {
        "name": "Channel 6",
        "folder_id": "1zamOEWf8pszbKI8Pvx8nH7WhuppN1F7h",
        "uploaded_folder_id": "12IWS02YpViX3_D24_QydVNQPxja_lds8",
        "token": TOKENS_DIR / "channel6.json",
        "privacy": "public"
    },

    "channel7": {
        "name": "Channel 7",
        "folder_id": "1EcyW3uXMPwYlECrAaHS1Rh50zat08gIJ",
        "uploaded_folder_id": "1f6NxX6YYirgyXzfwb2toj_lXL2_MZye6",
        "token": TOKENS_DIR / "channel7.json",
        "privacy": "public"
    },

    "channel8": {
        "name": "Channel 8",
        "folder_id": "15076k_JTcPC_QudAU5bwf8XJxaPC40Oe",
        "uploaded_folder_id": "1UoYe72brkcvkGFRcXVKZe-UxnogMdcwj",
        "token": TOKENS_DIR / "channel8.json",
        "privacy": "public"
    }

}
def list_files(self, folder_id):
    print("Received folder_id:", repr(folder_id))

    results = (
        self.service.files()
        .list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields="files(id,name,mimeType)"
        )
        .execute()
    )

    return results.get("files", [])