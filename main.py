from pyrogram import Client, filters
import tgcrypto
from pyrogram.types import Message
import base64
import os
import json
from pyromod import listen
from keep import keep_alive
bot = Client(
    api_id=os.environ.get("API_ID"),
    api_hash=os.environ.get("HASH"),
    bot_token=os.environ.get("TOKEN"),
    session_name=":memory:",
)
black = os.environ.get("BLACK")
owner = os.environ.get("OWNER_ID")
chat_id = os.environ.get("CHAT_ID")

@bot.on_message(filters.command("delete") & filters.private)
async def delo(bot, message):
   code = await bot.ask(message.chat.id, "Send me the **Secret**!")
   code = str(code.text)
   code = code.encode("ascii")
   codm=base64.b64decode(code)
   print("1 done")
   codq=base64.b64decode(codm).decode("ascii")
   print(codq)
   o =await bot.get_messages(chat_id, int(codq))
   
   m =await bot.delete_messages(chat_id, int(codq))
   print(m)
   if m == True:

   elif m == False:
    
   else:
    print("crap")
   
   await message.reply_text("Deleted")
   await bot.send_message(owner, f"Message deleted, ID: {codq}")
if __name__ == "__main__": 
  keep_alive()
  bot.run()
   
