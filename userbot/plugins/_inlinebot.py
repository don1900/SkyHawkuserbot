
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from math import ceil
from re import compile
import asyncio

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import *
from userbot.cmdhelp import *
from TgxBot.utils import *
from userbot.Config import Config

Tgx_row = Config.BUTTONS_IN_HELP
Tgx_emoji = Config.EMOJI_IN_HELP
# thats how a lazy guy imports
# TgxUserbot

def button(page, modules):
    Row = Tgx_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{Tgx_emoji} " + pair  + f" {Tgx_emoji}", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"{Tgx_emoji} ⬅️𝙱𝙰𝙲𝙺 {Tgx_emoji}", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"•{Tgx_emoji} ✖️𝙲𝙻𝙾𝚂𝙴✖️ {Tgx_emoji}•", data="close"
            ),
            custom.Button.inline(
               f"{Tgx_emoji} 𝙽𝙴𝚇𝚃➡️ {Tgx_emoji}", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in TgxUserbot channel to get this module work...

    modules = CMD_HELP
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@TgxUserbot":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"**▪Tgx 🦅 𝚄𝚂𝙴𝚁𝙱𝙾𝚃▪**\n\n__𝚃𝚘𝚝𝚊𝚕 𝚙𝚕𝚞𝚐𝚒𝚗𝚜 𝚒𝚗 𝚢𝚘𝚞𝚛 𝚞𝚜𝚎𝚛𝚋𝚘𝚝__ :`{len(CMD_HELP)}`\n**page:** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        else:
            result = builder.article(
                "@FURIOUS_X_Y",
                text="""**Hey! This is [Tgx Userbot.](https://t.me/Tgx_Updates) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 CHANNEL 🔥", "https://t.me/Tgx_Updates"),
                        custom.Button.url(
                            "⚡ 👥 GROUP 👥", "https://t.me/TgxSupport"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "🔥 REPO 🔥", "https://github.com/don1900/Tgx"),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "DEKH KYA RAHE HO YRR JAO AUR APNA Tgx BOT DEPLOY KARO AUR MAJA LO 🤓",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**𝚈𝙾𝚄𝚁** [ꜱᴋʏʜᴀᴡᴋ ᴜꜱᴇʀʙᴏᴛ](https://t.me/Tgx_Updates) __Working...__\n\n**Number of modules installed :** `{len(CMD_HELP)}`\n**page:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )
        
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_Tgx(event,
              "**Tgx Help Menu**\n\n         **[(ℂ)𝕊𝕜𝕪ℍ𝕒𝕨𝕜™](t.me/Tgx_Updates)**", 5, link_preview=False
            )
        else:
            Tgx_alert = "Bas laga liya dimaag? Itni der se tip tip kar rahe ho. Jao khud ka bana lo na yrr. 𝕊𝕜𝕪ℍ𝕒𝕨𝕜™"
            await event.answer(Tgx_alert, cache_time=0, alert=True)
          
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "DEKH KYA RAHE HO YRR JAO AUR APNA Tgx BOT DEPLOY KARO AUR MAJA LO (ℂ)𝕊𝕜𝕪ℍ𝕒𝕨𝕜™ ",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "✘ " + cmd[0] + " ✘", data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline(f"{Tgx_emoji} 𝐁𝐀𝐂𝐊 {Tgx_emoji}", data=f"page({page})")])
        await event.edit(
            f"**🗂 Module:** `{commands}`\n**🔢 Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "DEKH KYA RAHE HO YRR JAO AUR APNA Tgx BOT DEPLOY KARO AUR MAJA LO 𝕊𝕜𝕪ℍ𝕒𝕨𝕜™ ",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**🗂 Modules:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**✅Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"**🚫 Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**🚫 Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🧾 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**🧾 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**💬 USE:** `{command['usage']}`\n\n"
        else:
            result += f"**💬 USE:** `{command['usage']}`\n"
            result += f"**⌨️ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline(f"{Tgx_emoji} 𝙱𝙰𝙲𝙺 {Tgx_emoji}", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )


# Ask owner before using it in your codes
# Kangers like LB stay away...
