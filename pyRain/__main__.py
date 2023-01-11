import time
from . import *
from .modules import start, chatbot, listen, repo, help
from pyrogram import idle, Client
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger

LOGS = getLogger("pyRainloge")
_LOG_FORMAT = "%(asctime)s | %(name)s [%(levelname)s] : %(message)s"
    basicConfig(
        format=_LOG_FORMAT,
        level=INFO,
        datefmt="%m/%d/%Y, %H:%M:%S",
        handlers=[FileHandler(file), StreamHandler()],
    )

session = ClientSession()
rain.start()
LOGS.info(f"Took {time_formatter((time.time() - start_time)*1000)} to start Rain")
LOGS.info(
    """
            ----------------------------------------------------------------------
                Ultroid has been deployed! Visit @TheUltroid for updates!!
            ----------------------------------------------------------------------
"""
)
idle()
