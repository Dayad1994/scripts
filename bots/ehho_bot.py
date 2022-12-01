# скрипт для телебота, который дублирует текст юзера
import telebot
import os

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('bot_token')

bot = telebot.TeleBot(token)


@bot.message_handler(comands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что нибудь )')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


bot.polling(non_stop=True, interval=0)
