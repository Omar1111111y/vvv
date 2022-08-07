import os
import random
import requests
import json
from bot_imop import * 
#from tkinter import filedialog
#from duce import * 
bot = telebot.TeleBot(botmm)
def rmm(ms):
	iff = ms.text
	bot.reply_to(ms,'مطور هذا البوت عمر ستايل')
	os.system('python duce.py')
	bot.reply_to(ms,'تم التشغيل')
