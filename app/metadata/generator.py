import random

from .channel1 import TITLES as CHANNEL1_TITLES
from .channel2 import TITLES as CHANNEL2_TITLES
from .channel3 import TITLES as CHANNEL3_TITLES
from .channel4 import TITLES as CHANNEL4_TITLES
from .channel5 import TITLES as CHANNEL5_TITLES
from .channel6 import TITLES as CHANNEL6_TITLES
from .channel7 import TITLES as CHANNEL7_TITLES
from .channel8 import TITLES as CHANNEL8_TITLES


TITLE_BANK = {
    "channel1": CHANNEL1_TITLES,
    "channel2": CHANNEL2_TITLES,
    "channel3": CHANNEL3_TITLES,
    "channel4": CHANNEL4_TITLES,
    "channel5": CHANNEL5_TITLES,
    "channel6": CHANNEL6_TITLES,
    "channel7": CHANNEL7_TITLES,
    "channel8": CHANNEL8_TITLES,
}


DESCRIPTION = """
❤️ Thanks for watching!

Don't forget to Like 👍
Share 📤
Subscribe 🔔

#shorts
"""

TAGS = [
    "shorts",
    "viral",
    "trending"
]


class MetadataGenerator:

    def generate(self, channel_name: str):

        if channel_name not in TITLE_BANK:
            raise ValueError(f"Unknown channel: {channel_name}")

        return {
            "title": random.choice(TITLE_BANK[channel_name]),
            "description": DESCRIPTION,
            "tags": TAGS
        }