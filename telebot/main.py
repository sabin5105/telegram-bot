from pydoc import doc
import telegram
import json
import time

import scrapper


TOKEN = None
chat_id = []

with open("token_ID.json", "r") as ti:
    ti = json.load(ti)
    TOKEN = ti["TOKEN"]
    chat_id.append(ti["CHAT_ID"])
    
bot = telegram.Bot(token=TOKEN)



def main():
    Seoultech = scrapper.Seoultech()
    
    while(Seoultech.check_title_of_announcement()):
        parse_data = Seoultech.get_title()
        bot.sendMessage(chat_id=chat_id[0], text=parse_data)
        time.wait(60)
        

if __name__ == "__main__":
    main()