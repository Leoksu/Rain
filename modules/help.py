from .stuff.string import HELP_TEXT
from pyrogram import Client, filters

@Client.on_message(filters.command("help"))
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
