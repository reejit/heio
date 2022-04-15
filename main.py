from pyrogram import Client, filters
import tgcrypto
from pyrogram.types import Message
import base64
import os
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
async def del(bot, message: Message):
   code = await client.ask(message.chat.id, "Send me the **Secret**!").text
   try:
     code = code.encode("ascii")
     codm=base64.b64decode(code)
     codq=base64.b64decode(codm).decode("ascii")
     print(codq)
     try:
      int(codq)
     except Exception as e:
       print(e)
       await message.reply_text("Please supply a valid code")
   except:
     pass

   try:
     await bot.get_messages(chat_id, codq)
     await bot.delete_messages(chat_id, codq)
     await message.reply_text("Deleted")
     await bot.send_message(owner, f"Message deleted, ID: {codq}")
   except Exception as e:
     print(e)
     await message.reply_text("Message Id not found")
     
if __name__ == "__main__": 
  keep_alive()
  bot.run()
   
