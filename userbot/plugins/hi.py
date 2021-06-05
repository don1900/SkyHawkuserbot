import random, re
from SkyhawkBot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern=r"hi$", outgoing=True))
async def _(event):
    if event.fwd_from:
        await event.edit("""HI HOW ARE YOU""")
        await asyncio.sleep(1)
        await ult.edit("""🌺✨✨🌺✨🌺🌺🌺
                          🌺✨✨🌺✨✨🌺✨
                          🌺🌺🌺🌺✨✨🌺✨
                          🌺✨✨🌺✨✨🌺✨
                          🌺✨✨🌺✨🌺🌺🌺
                          ☁️☁️☁️☁️☁️☁️☁️☁️"""
