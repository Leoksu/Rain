from decouple import config

AI_API_KEY = config("AI_API_KEY", default=None)
AI_BID = config("AI_BID", default=None, cast=int)
API_ID = config("API_ID", default=6)
API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
bot_token = config("BOT_TOKEN", default=None)
UPDATES_CHANNEL = config("UPDATES_CHANNEL", default="GhostWebs")
USERNAME = config("USERNAME", default=None)
