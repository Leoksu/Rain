from stuff.striny import HELP_TEXT
from pyrogram import Client, filters

@Client.on_message(filters.command("help") & ~filters.edited)
async def start(_, message):
    await message.reply_text(f"(HELP_TEXT}\n\n• @TheGhostOrg")
