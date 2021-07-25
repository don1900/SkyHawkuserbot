from ..utils import admin_cmd
@bot.on(admin_cmd(pattern='gcast'))
async def broadcast(event):
  Don = event.text.split(" ", 1)[1]
  async for Don19 in bot.iter_dialogs():
     if not Don19.is_group:
       continue
     fail = 0
     succ = 0
     chat = PROBOYX.id
     if Don19.is_channel:
       pass
     try:
        await bot.send_message(chat, Pro)
        succ += 1
     except:
        fail += 1
        pass
  await event.edit(f' done = {succ}\n fail = {fail}')

  CmdHelp("gcast").add_command(
 'gcast', None, 'Globally Cast The Message'
  ).add()
