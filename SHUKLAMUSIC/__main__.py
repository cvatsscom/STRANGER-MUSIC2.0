import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from SHUKLAMUSIC import LOGGER, app, userbot
from SHUKLAMUSIC.core.call import SHUKLA
from SHUKLAMUSIC.misc import sudo
from SHUKLAMUSIC.plugins import ALL_MODULES
from SHUKLAMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝗔𝗕𝗘 𝗟𝗢𝗗𝗘 𝗦𝗧𝗥𝗜𝗡𝗚 𝗧𝗘𝗥𝗔 𝗕𝗔𝗣 𝗗𝗔𝗟𝗘 𝗚𝗔 𝗞𝗬𝗔 😑")
        
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SHUKLAMUSIC.plugins" + all_module)
    LOGGER("SHUKLAMUSIC.plugins").info("")
    await userbot.start()
    await SHUKLA.start()
    await SHUKLA.decorators()
    LOGGER("SHUKLAMUSIC").info(
        ""
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SHUKLAMUSIC").info("")
    

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
