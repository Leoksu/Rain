from pyrogram import Client
from config import API_ID, API_HASH, bot_token

ghoul = Client(
    "VideoPlayer",
    API_ID,
    API_HASH,
    bot_token=bot_token
)
ghoul.start()
rain = ghoul.get_me()
USERNAME = rain.username
BOT_NAME = rain.first_name
