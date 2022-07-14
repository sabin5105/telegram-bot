import telegram
import json

TOKEN = None
chat_id = []
with open("token_ID.json", "r") as ti:
    ti = json.load(ti)
    TOKEN = ti["TOKEN"]
    chat_id.append(ti["CHAT_ID"])
    
bot = telegram.Bot(token=TOKEN)

text_message = "Hello World"
bot.sendMessage(chat_id=chat_id[0], text=text_message) # send message to chat_id