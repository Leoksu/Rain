import asyncio
from datetime import datetime
from pyrogram import Client, filters

PING_DELAY_DELETE = 8
START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
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
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


main_filter = (
    filters.text
    & filters.incoming
    & ~filters.edited
)

@Client.on_message(main_filter & filters.regex("^/uptime$"))
async def get_uptime(_, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = _human_time_duration(int(uptime_sec))
    await message.reply_text(f"**Uptime**: `{uptime}`\n"
                             f"**Start time**: `{START_TIME_ISO}`",
                             quote=True)
