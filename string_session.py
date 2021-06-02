from telethon.sync import TelegramClient
from telethon.sessions import StringSession


print("Hey!,Welcome to SkyHawk Userbot String Generator\n\nBy @always_don")
print("\n🔥 SkyHawk Userbot 🔥\n\nProperly Enter Your Details.\n")

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
try:
  API_ID = int(input("Enter Your API ID here: "))
  API_HASH = input("\nEnter Your API HASH here: ")
  with TelegramClient(StringSession(), API_ID, API_HASH) as SkyHawk:
    SkyHawksession = SkyHawk.session.save()

    SkyHawk = SkyHawk.send_message("me",f"\n\n😎Your String Session Here👇\n\n```{SkyHawksession}```\n\n🔥🔥🔥Tap It To Copy🔥🔥🔥\n        **Regards @always_don**")


  print("\n\nWe Have Sent Your String Session At Your Saved Message Check It Out.\n\n            NOTE:Store It In A Safe Place!")

except :
    print("\nThe Details You Provided Were Wrong \nPlease Try Again")
   
