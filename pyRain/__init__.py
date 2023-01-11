from pyrogram import Client, errors
from .. import 
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


rain = Client(
    ".RainSession",
    bot_token=bot_token,
    api_id=API_ID,
    api_hash=API_HASH,
)

bot_id = int(bot_token.split(":")[0])
