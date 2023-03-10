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

TOKEN = "5952042833:AAF1Gv-BeTz3S_2Y_dVKswGdJ0S7tR9WPX0"
bot = telebot.TeleBot(TOKEN)

def getargs(text):
	_args = text.split()[1:]
	return _args


@bot.message_handler(commands=["start"])
def get_user_info(message):
  response = requests.get('https://sun9-east.userapi.com/sun9-20/s/v1/ig2/gzu19FdXcV8QQ97z06TAuNOs28ek6vaP4C4WMxWgTogHRzu-zt31UMNYjZqDcJFaHNhMOrQL7eQi34KLGk14Nd29.jpg?size=1080x1080&quality=95&type=album')
  imgnet = Image.open(BytesIO(response.content))
  bot.send_photo(message.chat.id, imgnet)

  markup_inline2 = types.InlineKeyboardMarkup()
  item_0 = types.InlineKeyboardButton(text = 'Хочу предсказание', callback_data = '1')
  markup_inline2.add(item_0)

  bot.send_message(message.chat.id, "✨Дорогие наши коллеги и друзья!✨\n\
Команда Dazzling поздравляет вас с наступающим Новым годом и Рождеством!🎁\n\
Новый год - Новые желания и новые возможности!💫\n\
Это был неоднозначный год, пусть в следующем году будет больше ясности и все будут лучше друг друга слышать🎄\n\
🎀Пусть в мире будет больше любви и любовь будет в мире!🎀\n\
\n\
Попытайте удачу и получите ваше личное предсказание на 2023 год от нашего волшебного бота🔮", reply_markup = markup_inline2)
 
  #bot.send_message(message.chat.id,"Хотите получить личное предсказание на 2023 год? Нажимайте рандомную кнопку, чтобы выбрать предсказание и переходите по ссылке)", 
                   #reply_markup = markup_inline)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
  if call.data == '1':
      urlslist = ['https://telegra.ph/Esli-vy-sosredotochites-na-tom-chto-u-vas-est-vy-vsegda-poluchite-bolshe-Esli-vy-dumaete-o-tom-chego-net-vam-nikogda-ne-budet-do-12-27','https://telegra.ph/Ne-menyaya-napravleniya-ty-ostaeshsya-na-tom-zhe-meste-12-27','https://telegra.ph/Dlya-pobedy-nedostatochno-byt-silnym-Vsya-komanda-dolzhna-verit-v-pobedu-12-27',
              'https://telegra.ph/Tvorchestvo-zarazitelno-Peredajte-ehto-12-27','https://telegra.ph/Sekret-uspeha--sdelat-pervyj-shag-12-27','https://telegra.ph/Zazhgi-zavtra-segodnyashnim-dnem-12-27','https://telegra.ph/Stremites-k-bolee-vysokomu-urovnyu-kazhdyj-den-prinimaya-kazhdoe-reshenie-Bolshoj-i-malenkij-nash-vybor-uvelichivaet-nashu-zhizn-12-27',
              'https://telegra.ph/Kazhdyj-den---ehto-otlichnaya-vozmozhnost-12-27','https://telegra.ph/Magiya---ehto-vera-v-sebya-Esli-ty-smozhesh-ehto-sdelat-ty-smozhesh-sdelat-vse-chto-ugodno-12-27','https://telegra.ph/Segodnya-ne-prosto-eshche-odin-den-EHto-novaya-vozmozhnost-eshche-odin-shans-novoe-nachalo-Primi-ehto-12-27']
      markup_inline = types.InlineKeyboardMarkup()
      item_1 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))
      item_2 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))
      item_3 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))
      item_4 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))
      item_5 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))
      item_6 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))
      item_7 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))
      item_8 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))
      item_9 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))
      item_10 = types.InlineKeyboardButton(text = '🥠', callback_data = '1', url = random.choice(urlslist))

      markup_inline.add(item_1) 
      bot.send_message(call.message.chat.id,"Ваше личноe предсказание на 2023 год готово. Нажимайте на кнопку и переходите по ссылке🎁", 
                      reply_markup = markup_inline)

  elif call.data == '2':
    pass


@bot.message_handler(commands=["helpmepls"])
def sayhelp(message):
	bot.send_message(message.chat.id, "There are no help. How dare are you, pig.")
	
@bot.message_handler(commands=["madeby"])
def sayhelp(message):
	bot.send_message(message.chat.id, "I was made by Maxim Si.")

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
