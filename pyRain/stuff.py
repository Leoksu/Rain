import pyrogram

SOURCE='https://t.me/TheGhostOrg'

HELP_TEXT="""
-- **Start Conversation** --

\u2022 Want to chatting with me?
\u2022 Just send a chat to start conversation
\u2022 You can also use me in groups
\u2022 Add me to your groups and send `/start`
\u2022 Then you can chatting with me by reply my chat

\u2022\u2022 You also can call me without reply to me or send any command
  \u2022 - Just call my name in your groups and i will come to you
  \u2022 - You need to make me admin in your grouos to use this


-- **Available Commands**: --

\u2022 `/start` - Start the bot
\u2022 `/help` - Send this help message
\u2022 `/repo` - Get the source code of this bot
\u2022 `/manage` - Developers only
 """

ABOUT_TEXT=f"-- **Informations** --\n\n**Rain** | `Nameless Ghoul(Water)`\n\n- **Rain** is a `Telegram` Chat Bot that made for fun only(not contain search engine or `ChatGPT`-like stuff)\n- Written in `Python` language with `Pyrogram` library, Using `brainshop.ai` API for generating responses\n\n**This bot licensed under [GNU-GPL](https://www.gnu.org/license/) 3.0 License!**\n**Developed by [Ghost.org](t.me/{UPDATES_CHANNEL})**"

def START_TEXT(message):
    mention = message.from_user.mention
    return f"**Hello {mention}!**\nMy name is **Rain** also known as `Nameless Ghoul(Water)`.\nI'm One of `The Eight Ghouls` from @TheGhostOrg.\nI like to chat, maybe I can make you happy?\nLet's start some fun conversation.\n\n\u2022 **@TheGhostOrg**"

MENU_TEXT= "**Main Menu!**\nMy name is **Rain** also known as `Nameless Ghoul(Water)`.\nI'm One of `The Eight Ghouls` from @TheGhostOrg.\nI like to chat, maybe I can make you happy?\nLet's start some fun conversation.\n\n\u2022 **@TheGhostOrg**"

