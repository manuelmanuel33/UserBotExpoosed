"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`𝔏𝔦𝔳𝔢 𝔞𝔰 𝔦𝔣 𝔶𝔬𝔲 𝔴𝔢𝔯𝔢 𝔱𝔬 𝔡𝔦𝔢 𝔱𝔬𝔪𝔬𝔯𝔯𝔬𝔴. 𝔏𝔢𝔞𝔯𝔫 𝔞𝔰 𝔦𝔣 𝔶𝔬𝔲 𝔴𝔢𝔯𝔢 𝔱𝔬 𝔩𝔦𝔳𝔢 𝔣𝔬𝔯𝔢𝔳𝔢𝔯.👍STO BENE, BOSS🎈🎈`**\n\n"
                     "**✅Telethon version:- 6.9.0**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**✅Python: 3.7.3**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**✅Bot CREATO DA:- @EXPOOSED\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**"
                     "**✅Database Status: Databases functioning normally!**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n💞SEMPRE CON TE BOSS!\n`"
                     f"`CHI MI HA ATTIVATO`: {DEFAULTUSER}\n"
                     "[GRANDE, BOSS")
