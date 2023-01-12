
import re
import requests
from pyrogram import Client, filters 
from asyncio import sleep
from config import AI_BID, AI_API_KEY, bot_token

bot_id=int(bot_token.split(":")[0])

async def rainchat(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    r = requests.get(f"http://api.brainshop.ai/get?bid={AI_BID}&uid={message.from_user.id}&key={AI_API_KEY}&msg={message.text}")
    rain = r.json()["cnt"]
    await sleep(2)
    try:
        await message.reply_text(f"{rain}")
    except Exception as e:
        await message.reply_text(f"An error occurred : {e}")
        return
    await message._client.send_chat_action(chat_id, "cancel")

@Client.on_edited_message(
    ~filters.private,
    ~filters.text,
    ~filters.command("help"),
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}rain[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await rainchat(message)

@Client.on_edited_message(filters.private & ~filters.command("help"))
async def chatpm(_, message):
    if not message.text:
        return
    await rainchat(message)
