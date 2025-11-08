import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "520697782").split()))

API_ID = int(os.getenv("API_ID", "35654751"))

API_HASH = os.getenv("API_HASH", "8f048d469ca9a1f85fc15172fc32e1df")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8393797496:AAFf2P8sWGmNmwK4RCDF4-Bl9XbDCe6COjY")

OWNER_ID = int(os.getenv("OWNER_ID", "520697782"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "").split()))

RMBG_API = os.getenv("RMBG_API", "MA2sUZ4HdAfBegL36HiG4BUG")

MONGO_URL = os.getenv("MONGO_URL", "mongosh "mongodb+srv://Testing:Ubotin@cluster0.7agqclm.mongodb.net/?retryWrites=true&w=majority")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4628173231"))
