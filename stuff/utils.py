from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

ghoul = Client(
    "VideoPlayer",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN
)
ghoul.start()
rain = ghoul.get_me()
USERNAME = rain.username
BOT_NAME = rain.first_name
