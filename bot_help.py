from bot_imop import *
from bot_detd import *
#from mys import *
###############
#print(botmm)
bot = telebot.TeleBot(botmm)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, """ Omar_Style هلا مرحباب""")
#       m =bot.reply_to(message)
#       if m == "omar":
#               bot.reply_to(message,"ok ok")
@bot.message_handler(func=lambda ms: True)
###################~########
##################
def echo_all(ms):
######
        #omar(message)
	#emil(ms)
	rmm(ms)
####
bot.infinity_polling()
