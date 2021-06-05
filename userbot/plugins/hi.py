import random, re
from SkyhawkBot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="hi ?(.*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("""HI HOW ARE YOU""")
        await asyncio.sleep(1)
        await ult.edit("""🌺✨✨🌺✨🌺🌺🌺
                          🌺✨✨🌺✨✨🌺✨
                          🌺🌺🌺🌺✨✨🌺✨
                          🌺✨✨🌺✨✨🌺✨
                          🌺✨✨🌺✨🌺🌺🌺
                          ☁️☁️☁️☁️☁️☁️☁️☁️"""
                      
CmdHelp("hi").add_command(
  'hi', 'Gives A Hi Animation.'
).add(
 
