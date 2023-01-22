from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters
from .stuff.string import *
from .stuff.config import *



@Client.on_message(
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

@Client.on_callback_query()
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
