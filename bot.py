from pyrogram import Client, idle
from pyromod import listen
from casery import caes, casery, group, source, photosource, caserid, ch, bot_token, bot_token2

bot = Client("CAR", api_id=17784375, api_hash="f4979d23cf6e9c58fcf7886f123cdee6", bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=17784375, api_hash="f4979d23cf6e9c58fcf7886f123cdee6", session_string=bot_token2)    

DEVS = caes
DEVSs = []
bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(casery, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()
