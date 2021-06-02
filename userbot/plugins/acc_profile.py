'''Profile Updating Commands
.pbio <Enter The Bio You Want To Put> 
.pname <Enter The Name You Want To Put>
.ppic 
'''

import os
from telethon import events
from telethon.tl import functions
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="pbio (.*)"))  
async def _(event):
    if event:
        return
    bio = event.pattern_match.group(1)
    try:
        await borg(functions.account.UpdateProfileRequest(  
            about=bio
        ))
        await event.edit("`Hey Master!Successfully Changed Your Bio")
    except Exception as e:  
        await event.edit(str(e))


@borg.on(admin_cmd(pattern="pname ((.|\n)*)"))  
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if  "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await borg(functions.account.UpdateProfileRequest( 
            first_name=first_name,
            last_name=last_name
        ))
        await event.edit("Hey Master!Successfully Changed Your Name")
    except Exception as e:  
        await event.edit(str(e))


@borg.on(admin_cmd(pattern="ppic"))  
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("Downloading this photo...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  
    photo = None
    try:
        photo = await borg.download_media(  
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY  
        )
    except Exception as e:  
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("Uploading your Profile Photo ...")
            file = await borg.upload_file(photo)  
            try:
                await borg(functions.photos.UploadProfilePhotoRequest(  
                    file
                ))
            except Exception as e:  
                await event.edit(str(e))
            else:
                await event.edit("Hey Master!Your profile picture has benn changed succesfully")
    try:
        os.remove(photo)
    except Exception as e:  
        logger.warn(str(e))  

except:
    await event.edit("*An error occoured*")
    time.sleep(0.9)
    await event.edit("Plz Try again!!")


# @borg.on(admin_cmd(pattern="pusername ((.|\n)*)"))  
# async def _(event):
#     if event.fwd_from:
#         return
#     username = event.pattern_match.group(1)
#     try:
#         await borg(functions.account.UpdateProfileRequest( 
#             username=username
#         ))
#         await event.edit("Hey Master!Your Username Has Been Changed Succesfully")
#     except:
#         await event.edit("*The Username You gave *")
#         time.sleep(0.9)
#         await event.edit("Plz Try again!!")

