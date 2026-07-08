from app.youtube import YouTubeAuth
from app.config import TOKENS_DIR

auth = YouTubeAuth(
    TOKENS_DIR / "channel9.json"
)

credentials = auth.authenticate()

print("Authentication Successful")