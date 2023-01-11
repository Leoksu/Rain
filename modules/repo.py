from pyrogram import Client, filters
from stuff.string import SOURCE
from config import UPDATES_CHANNEL

@Client.on_message(filters.command("repo") & ~filters.edited)
async def repo(_, message):
    await message.reply_text(
        "Repository is currently hidden\n"
        + f" [GitHub](t.me/{SOURCE})"
        + f" | [Channel](t.me/{UPDATES_CHANNEL})",
        disable_web_page_preview=True,
    )
