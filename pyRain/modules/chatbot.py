from .. import rain 



async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    r = requests.get(f"http://api.brainshop.ai/get?bid={AI_BID}&uid={message.from_user.id}&key={AI_API_KEY}&msg={message.text}")
    hey = r.json()["cnt"]
    await sleep(2)
    try:
        await message.reply_text(f"{hey}")
    except Exception as e:
        print(f"An error occurred : {e}")
        return
    await message._client.send_chat_action(chat_id, "cancel")
