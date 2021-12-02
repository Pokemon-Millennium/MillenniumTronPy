#Versione alternativa del bot in python
from json import load
import telebot
from os import path

DIRECTORY = path.dirname(path.abspath(__file__))+"/"

def jread(file) -> dict:
    """Legge un file json e ritorna il dizionario corrispondente. Il nome deve essere fornito con path relativo rispetto al file py e senza estensione"""
    with open(DIRECTORY+file+".json",encoding="utf-8") as temp_file:
        data=load(temp_file)
    return data

settings_dict=jread("settings")#Legge il file settings.json

bot=telebot.TeleBot(settings_dict["token"])

@bot.message_handler(commands=["start"])
def start(message):
    print(message)
    bot.stop_polling()

bot.polling()