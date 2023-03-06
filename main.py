#!pip install pyTelegramBotAPI
#pip install requests
#pip install Pillow

import time
import telebot
from telebot import types
from PIL import Image
import requests
from io import BytesIO
import random

TOKEN = "6024345369:AAF__ShNzfEBIoKVB3tNETNqZNcc7-CRuWY"
bot = telebot.TeleBot(TOKEN)

def getargs(text):
	_args = text.split()[1:]
	return _args


@bot.message_handler(commands=["start"])
def get_user_info(message):

  markup_inline2 = types.InlineKeyboardMarkup()
  item_0 = types.InlineKeyboardButton(text = '🍀', callback_data = '1')
  markup_inline2.add(item_0)

  bot.send_message(message.chat.id, "✨Дорогая, вся наша женская команда поздравляет тебя с праздником весны!✨\n\
Мы приготовили подарок и он про искусство.🎁\n\
Черпай вдохновение из проверенных источников) и наполняйся новыми!💫\n\
Чтобы получить подарок - испытай удачу!\n\
🎀Пришли нам клевер 🍀 в ответ на сообщение и следуй дальнейшим инструкциям.🎀\n\
\n\
Удачи!", reply_markup = markup_inline2)

  #bot.send_message(message.chat.id,"Хотите получить личное предсказание на 2023 год? Нажимайте рандомную кнопку, чтобы выбрать предсказание и переходите по ссылке)", 
                   #reply_markup = markup_inline)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
  markup_inline3 = types.InlineKeyboardMarkup()
  item_0 = types.InlineKeyboardButton(text = '❤️', callback_data = '1')
  markup_inline3.add(item_0)
  if call.data == '1':
    bot.send_message(message.chat.id, "Вращай "Колесо Фортуны" и выигрывай незабываемые впечатления!\n\
Ура! Ты выиграла главный приз!\n\
Пришли нам в ответ на это сообщение - сердечко ❤️ и порадуйся вместе с нами!", reply_markup = markup_inline3)  
  elif call.data == '2':
    pass
@bot.callback_query_handler(func = lambda call: True)
def answer(call):
if call.data == '1':
    bot.send_message(message.chat.id, "Вращай "Колесо Фортуны" и выигрывай незабываемые впечатления!\n\
Ура! Ты выиграла главный приз!\n\
Пришли нам в ответ на это сообщение - сердечко ❤️ и порадуйся вместе с нами!", reply_markup = markup_inline3)  
  elif call.data == '2':
    pass


@bot.message_handler(commands=["helpmepls"])
def sayhelp(message):
	bot.send_message(message.chat.id, "There is no help. How dare are you, pig.")

@bot.message_handler(commands=["saythis"])
def textto_speech(message):
	args = getargs(message.text)
	text = " ".join(args[0:])
	try:
		bot.send_message(message.chat.id, text)
	except Exception as e:
		bot.send_message(message.chat.id, f"There was an exception")

while True:
	try:
		bot.polling()
	except:
		time.sleep(5)
