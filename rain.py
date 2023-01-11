import time
from pyrogram import Client, errors
from config import API_ID, API_HASH, bot_token
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
from aiohttp import ClientSession
from modules import chat, help, ping, repo, start

rain = Client(
    ".RainSession",
    bot_token=bot_token,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="modules")
)



LOGS = getLogger("pyRainloge")
_LOG_FORMAT = "%(asctime)s | %(name)s [%(levelname)s] : %(message)s"
basicConfig(
    format=_LOG_FORMAT,
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S",
)

session = ClientSession()
rain.start()
LOGS.info(f"Took {time_formatter((time.time() - start_time)*1000)} to start Rain")
LOGS.info(
    """
            ----------------------------------------------------------------------
                    Rain has been stared! Join @TheGhostOrg for updates!!
            ----------------------------------------------------------------------
"""
)
idle()
