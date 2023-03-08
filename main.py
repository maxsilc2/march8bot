#!pip install pyTelegramBotAPI
#!pip install requests
#!pip install Pillow

import time
import telebot
from telebot import types
from PIL import Image
import requests
from io import BytesIO
import random
import array

people = ["янина новицкая", "553482935724832", "полина крутских","виктория крихели","анастасия винниченко","дина павлова","кристина проскурякова","553482935724832","виктория одинцова","553482935724832","553482935724832","елена минченко","553482935724832","екатерина пескова","553482935724832","нургуль мартс","натали салий","марика","марина левочка","553482935724832","ирина микоян","екатерина кутумова","553482935724832","553482935724832","мария шишова","олеся панова","юля мошкович","ээээ"]
code = ["VBRE3CJD","UT5BQZ4N","649H82EN","EYP8EWAG","GQJSCKMH","APAMYQ2P","QX7GT6VS","VNUZQC4H","4QW9A7ER","WQFYHGR2","T6JRYX28","G8DX8NZ2","KSADA8F9","HK5ABAYW","Q2CZMJ92","95QGX7HM","TRZS22QU","M52EU3PV","DXVD3YF8","FJ5JA3JF","VBRE3CJD","M5SXG6NG","8Q2FMVAF","6QXKXPF4","4PTYDXAU","T3RMR9BJ","WW7JJNHN","эээээээээээ"]
TOKEN = "6024345369:AAF__ShNzfEBIoKVB3tNETNqZNcc7-CRuWY"
bot = telebot.TeleBot(TOKEN)


def download_file(url, name="video.mp4"):
    r = requests.get(url, stream=True)
    with open(name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)



def whatif(name):
    i=0
    while name != people[i] and i < len(people)-1:
             i += 1
    return i

@bot.message_handler(commands=["start"])
def get_user_info(message):

  markup_inline2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item_0 = types.KeyboardButton('🍀')
  markup_inline2.add(item_0)

  bot.send_message(message.chat.id, "✨Дорогая, вся наша женская команда поздравляет тебя с праздником весны!✨\n\
Мы приготовили подарок и он про искусство.🎁\n\
Черпай вдохновение из проверенных источников) и наполняйся новыми!💫\n\
Чтобы получить подарок - испытай удачу!\n\
🎀Пришли нам клевер 🍀 в ответ на сообщение и следуй дальнейшим инструкциям.🎀\n\
\n\
Удачи!", reply_markup = markup_inline2)

@bot.message_handler(content_types=['text'])
def get_text(message):
  if message.text == '🍀':
       markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
       item_1 = types.KeyboardButton('❤️')
       markup_reply.add(item_1) 
       bot.send_message(message.chat.id,"Вращай Колесо Фортуны и выигрывай незабываемые впечатления!")
       download_file("https://instagram.ftas2-1.fna.fbcdn.net/o1/v/t16/f1/m82/9749A770FEB768336D57A6EB96EC3F83_video_dashinit.mp4?efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uNzIwLmNsaXBzLmJhc2VsaW5lIn0&_nc_ht=instagram.ftas2-1.fna.fbcdn.net&_nc_cat=104&vs=1276778489591918_578504870&_nc_vs=HBksFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC85NzQ5QTc3MEZFQjc2ODMzNkQ1N0E2RUI5NkVDM0Y4M192aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVABgkR0hQMTlCUEhrbU1IMzFZRUFNWDZSODdUMUVZbGJxX0VBQUFGFQICyAEAKAAYABsAFQAAJurYruib2fo%2FFQIoAkMzLBdARQQ5WBBiThgSZGFzaF9iYXNlbGluZV8xX3YxEQB1%2FgcA&_nc_rid=56c20f6578&ccb=9-4&oh=00_AfCCUqIzWt6SKgUhwFYmrTsKxMKZKeGnF_BM6RcHtF6WNg&oe=640A34DF&_nc_sid=30a2ef", "fortune.mp4")
       vidnet = open("fortune.mp4", "rb")
       bot.send_video(message.chat.id, vidnet)
       time.sleep(50)
       bot.send_message(message.chat.id,"Ура! Ты выиграла главный приз!")
       bot.send_message(message.chat.id,"Пришли нам в ответ на это сообщение - сердечко ❤️ и порадуйся вместе с нами!", 
                      reply_markup = markup_reply)
  elif message.text == '❤️':
       bot.send_message(message.chat.id,"Успешной женщине, всегда улыбается удача)")
       bot.send_message(message.chat.id,"Пришли свое полное имя и фамилию русскими буквами (например: Мирослава Байда), чтобы получить свой Персональный подарок 💕")
  elif message.text.lower() == 'анастасия колтунова' or message.text.lower() == 'максим си' or message.text.lower() == 'макси':
       bot.send_message(message.chat.id, 'Привет создатель!')          
  elif whatif(message.text.lower())<=26 :
       bot.send_message(message.chat.id, 'Поздравляем!')
       bot.send_message(message.chat.id, 'Этот весенний подарок от нашей команды создан специально для тебя!')
       bot.send_message(message.chat.id, ' Регистрируйся на понравившийся курс от наших друзей школы Masters, используя данный промокод')
       bot.send_message(message.chat.id, code[whatif(message.text.lower())])
       markup_inline2 = types.InlineKeyboardMarkup()
       item_0 = types.InlineKeyboardButton(text = 'инструкция по регистрации', callback_data = '1', url = 'https://docs.google.com/document/d/1zZ5hmAe_VFGwtfn5Vnsu6Wcm4KjFOCqPpsKiDo5GNnE/edit?usp=sharing')
       markup_inline2.add(item_0)
       bot.send_message(message.chat.id, '         Здесь 👇🏻', reply_markup = markup_inline2)
       bot.send_message(message.chat.id, 'Получай море вдохновения и весеннего настроения вместе с командой Dazzz')
  else :
       bot.send_message(message.chat.id, 'Я не нашел такого имени, попробуй ввести полное имя 🥺')

    



while True:
	try:
		bot.polling()
	except:
		time.sleep(5)
