"""This Command is Very Useful To Add User(s) To The Current Chat.
Syntax: .invite <User(s)>"""

from telethon import functions
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="invite ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit(".invite`You Can't Add User To Private Message 😅 Can Only Add in Chat`")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Requested User Added To Chat Succesfully!")
        else:
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Requested User Added To Chat Succesfully!")
