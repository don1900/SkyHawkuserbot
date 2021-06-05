# PLUGIN MADE BY @always_don FOR SkyhawkBot
# KEEP CREDITS ELSE GAY

import random, re
from SkyhawkBot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="bye ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("""I GOTTA GO!""")
        await asyncio.sleep(1)
        await ult.edit("""
 

██████╗░██╗░░░██╗███████╗
██╔══██╗╚██╗░██╔╝██╔════╝
██████╦╝░╚████╔╝░█████╗░░
██╔══██╗░░╚██╔╝░░██╔══╝░░
██████╦╝░░░██║░░░███████╗
╚═════╝░░░░╚═╝░░░╚══════╝
""")
