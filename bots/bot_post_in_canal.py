# бот постит в канал инфу с файла
# в коде нужно добавить ссылку на канал
# в канале добавить в подписчики бота и сделать его админом
import telebot
import time
import os

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('bot_token')

# Токен, который выдает @botfather
bot = telebot.TeleBot(token)
# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = '@dayad_17'
# Загружаем список шуток
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks_list = f.read().split('\n')
f.close()
# Пока не закончатся шутки, посылаем их в канал
for think in thinks_list:
    bot.send_message(CHANNEL_NAME, think)
    # Делаем паузу в один час
    time.sleep(1)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")
