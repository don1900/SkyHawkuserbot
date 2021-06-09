from SkyhawkBot.utils import admin_cmd
import asyncio
from telethon import events
from userbot.cmdhelp import CmdHelp

@borg.on(admin_cmd(pattern="hi ?(.*)"))
async def _(event):
    if event.fwd_from:
        await event.edit("""HI HOW ARE YOU""")
        await asyncio.sleep(1)
        await event.edit("""'🌺✨✨🌺✨🌺🌺🌺/n🌺✨✨🌺✨✨🌺✨/n🌺🌺🌺🌺✨✨🌺✨/n🌺✨✨🌺✨✨🌺✨/n🌺✨✨🌺✨🌺🌺🌺/n☁️☁️☁️☁️☁️☁️☁️☁️""")
        
CmdHelp("hi").add_command(
  'hi', "Gives A Hi Text"
).add()
