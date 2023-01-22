from time import time
from pyrogram import Client, filters

@Client.on_message(main_filter & filters.regex("^/ping$"))
async def ping_pong(_, message: Message):
    start = time()
    reply = await message.reply_text("...", quote=True)
    delta_ping = time() - start
    await reply.edit_text(f"**Pong!**\n`{delta_ping * 1000:.3f} ms`")
