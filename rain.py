import time
start_time = time.time()
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, errors, idle, filters
from stuff.config import *
from logging import INFO, WARNING, basicConfig, getLogger
from stuff.time import time_formatter
from asyncio import get_event_loop, sleep
from stuff.string import *

LOGS = getLogger("RainLogs")
LOGS.info("Starting Deployement")
rain = Client(
    ".RainSession",
    bot_token=bot_token,
    api_id=API_ID,
    api_hash=API_HASH,
)

bot_id=int(bot_token.split(":")[0])

print(LOGS.info("Initializing..."))
_LOG_FORMAT = "%(asctime)s | %(name)s [%(levelname)s] : %(message)s"
basicConfig(
    format=_LOG_FORMAT,
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S",
)

## ------------------ Chat function ---------------- ##
import re
import requests

bot_id=int(bot_token.split(":")[0])

async def rainchat(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    await message._client.send_chat_action(chat_id, "typing")
    r = requests.get(f"http://api.brainshop.ai/get?bid={AI_BID}&uid={user_id}&key={AI_API_KEY}&msg={message.text}")
    rain = r.json()["cnt"]
    await sleep(2)
    await message.reply_text(f"{rain}")
    await message._client.send_chat_action(chat_id, "cancel")

@rain.on_message(
    ~filters.private
    & filters.text
    & ~filters.regex(r'^/')
    & ~filters.edited,
    group=666
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    elif not message.text:
        chat_id = message.chat.id
        await rain.send_chat_action(chat_id, "typing")
        await sleep(2)
        await message.reply("I'm sorry, in current version I can only understand word. Tell @aethersghoul don't being lazy and update me.")
        await rain.send_chat_action(chat_id, "cancel")
    else:
        match = re.search(
            "[.|\n]{0,}rain[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await rainchat(message)

@rain.on_message(filters.private & ~filters.regex(r'^/') & ~filters.edited)
async def chatpm(_, message):
    if not message.text:
        chat_id = message.chat.id
        await rain.send_chat_action(chat_id, "typing")
        await sleep(2)
        await message.reply("I'm sorry, in current version I can only understand word. Tell @aethersghoul don't being lazy and update me.")
        await rain.send_chat_action(chat_id, "cancel")
    await rainchat(message)

## ------------------ Help modules ---------------- ##

@rain.on_message(
    filters.text
    & ~filters.edited
    & filters.command("help")
)
async def start(_, message):
    buttons = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="start"),
                InlineKeyboardButton ("Updates 🔔", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(
        HELP_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

## ------------------ ping modules ---------------- ##
@rain.on_message(
    filters.text
    & ~filters.edited
    & filters.command("ping")
)
async def ping_pong(_, message):
    start = time()
    reply = await message.reply_text("__Ping...__", quote=True)
    delta_ping = time() - start
    await reply.edit_text(f"**Pong!**\n`{delta_ping * 1000:.3f} ms`")

## ------------------ Uptime modules ---------------- ##
import asyncio
from datetime import datetime

START_TIME = datetime.utcnow()
TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_FORMAT = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)
def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_FORMAT:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'.format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@rain.on_message(
    filters.text
    & ~filters.edited
    & filters.command("ping"))
async def get_uptime(_, message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"**Uptime**: `{uptime}`\n"
        + f"**Start time**: `{START_TIME_ISO}`",
        quote=True
    )

## ------------------ Start modules ---------------- ##
@rain.on_message(
    filters.command(["start", f"start@{USERNAME}"])
    & ~filters.edited
)
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("❓ How To Use Me ❓", callback_data="help"),
            ],
            [
                InlineKeyboardButton("🔔 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("Source 📦",  url="https://github.com/Leoksu/Rain"),
            ],                                           # god watching u
            [
                InlineKeyboardButton("📜 About", callback_data="about"),
                InlineKeyboardButton("Close ❌", callback_data="close"),
            ],
            [
                InlineKeyboardButton("➕ Add Me To Your Group ➕", url=f"https://t.me/{USERNAME}?startgroup=true")
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   START_TEXT = stuff.START_TEXT(client, message)
   mention = message.from_user.mention
   await message.reply_text(
       START_TEXT,
       reply_markup=reply_markup
       )

@rain.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="start"),
                InlineKeyboardButton ("Updates 🔔", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="start"),
                InlineKeyboardButton ("Updates 🔔", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("❓ How To Use Me ❓", callback_data="help"),
            ],
            [
                InlineKeyboardButton("🔔 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("Source 📦",  url=f"https://github.com/Leoksu/Rain"),
            ],                                             # dude ??
            [
                InlineKeyboardButton("📜 About", callback_data="about"),
                InlineKeyboardButton("Close ❌", callback_data="close"),
            ],
            [
                InlineKeyboardButton("➕ Add Me To Your Groups ➕", url=f"https://t.me/{USERNAME}?startgroup=true")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
               MENU_TEXT,
               reply_markup=reply_markup
            )
        except MessaageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

@rain.on_message(
    filters.text
    & ~filters.edited
    & filters.command("repo")
    )
async def repo(_, message):
    await message.reply_text(
        "Want to make your own bot like Rain?\nDon't forget to read the license.\n\n"
        + f"**[GitHub](https://github.com/Leoksu/Rain)**"
        + f" | **[Updates](t.me/{UPDATES_CHANNEL})**",
        disable_web_page_preview=True
    )

async def main():
    await rain.start()
    LOGS.info(f"Successfully started Rain in {time_formatter((time.time() - start_time)*1000)}")
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
