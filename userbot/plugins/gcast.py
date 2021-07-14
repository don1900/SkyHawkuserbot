# made for SkyhawkBot
# credits - LEGENDX22 and PROBOYX22

from ..utils import admin_cmd
@bot.on(admin_cmd(pattern='gcast'))
async def broadcast(event):
  Pro = event.text.split(" ", 1)[1]
  async for PROBOYX in bot.iter_dialogs():
     if not PROBOYX.is_group:
       continue
     fail = 0
     succ = 0
     chat = PROBOYX.id
     if PROBOYX.is_channel:
       pass
     try:
        await bot.send_message(chat, Pro)
        succ += 1
     except:
        fail += 1
        pass
  await event.edit(f' done = {succ}\n fail = {fail}')
  
  CmdHelp("gcast").add_command(
 'gcast', None, 'Globally Cast The Message In Connected Chats'
  ).add()
