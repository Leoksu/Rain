import time
from pyrogram import Client, errors, idle
from config import API_ID, API_HASH, bot_token
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
from aiohttp import ClientSession
from modules import chat, help, ping, repo, start
from stuff.time import time_formatter
from asyncio import get_event_loop

start_time = time.time()
print("Starting...")
rain = Client(
    ".RainSession",
    bot_token="5883344099:AAH7gCUysw8FomNukaj3enwvVSHMUXr8uYg",
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="modules")
)

bot_id=int(bot_token.split(":")[0])

LOGS = getLogger("pyRainloge")
print(LOGS.info("Initializing..."))
_LOG_FORMAT = "%(asctime)s | %(name)s [%(levelname)s] : %(message)s"
basicConfig(
    format=_LOG_FORMAT,
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S",
)

async def main():
    session = ClientSession()
    await rain.start()
    LOGS.info(f"Took {time_formatter((time.time() - start_time)*1000)} to start Rain")
    LOGS.info(
        """
                ----------------------------------------------------------------------
                        Rain has been stared! Join @TheGhostOrg for updates!!
                ----------------------------------------------------------------------
    """
    )
    await idle()

loop = get_event_loop()
loop.run_until_complete(main())
