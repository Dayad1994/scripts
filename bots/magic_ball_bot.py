from aiogram import *
import config
from random import *

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова",
           "Даже не думай", "Предрешено", "Вероятнее всего", "Спроси позже",
           "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы",
           "Лучше не рассказывать", "По моим данным - нет", "Да",
           "Определённо да", "Знаки говорят - да", "Весьма сомнительно",
           "Сейчас нельзя предсказать", "Перспективы не очень хорошие",
           "Можешь быть уверен в этом", "Сконцентрируйся и спроси опять"]

bot = Bot(config.TOKEN)
bot = Dispatcher(bot)


@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.\nЗадайте вопрос')


@bot.message_handler()
async def answer_to_question(question: types.Message):
    await question.answer(choice(answers))


if __name__ == '__main__':
    executor.start_polling(bot, skip_updates=True)
