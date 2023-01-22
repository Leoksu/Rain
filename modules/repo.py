from pyrogram import Client, filters
from .stuff.config import *

@Client.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_text(
        "Want to make your own bot like Rain?\nDon't forget to read license.\n\n"
        + f" [GitHub](https://github.com/Leoksu/Rain)"
        + f" | [Channel](t.me/{UPDATES_CHANNEL})",
        disable_web_page_preview=True,
    )
