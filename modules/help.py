from stuff.string import HELP_TEXT
from pyrogram import Client, filters

@Client.on_message(filters.command("help"))
async def start(_, message):
    await message.reply_text(
              HELP_TEXT,
              disable_web_page_preview=true,
          )
