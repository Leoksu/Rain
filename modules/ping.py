from stuff.utils import USERNANE
from pyrogram import Client, filters
from pyrogram.types import Message
import time

start_time = time.time()

@Client.on_message(filters.command(["ping", "ping@{USERNAME}"]))
async def ping(client, message):
          response_start_time = time.time()
          message_id = message.message_id
          chat_id = message.chat.id
          rain = await message.reply_text("`Calculating...`")
          response_end_time = time.time()
          response_time = (response_end_time - response_start_time) * 1000
          uptime = time.time() - start_time
          rain_ping = f"**Response time**: `{response_time:.2f}ms`, **Uptime** : `{uptime:.2f}s` "
          await rain.edit(chat_id, message_id, rain_ping)
