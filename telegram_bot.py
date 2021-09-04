import random
import logging
import telebot
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

#=========================================ОБЩЕЕ=================================================

bot = telebot.TeleBot('1980859217:AAHKffL93dOcN_XdJA89Dqf2YgxFPb14__Q')
aiogrambot = Bot(token='1980859217:AAHKffL93dOcN_XdJA89Dqf2YgxFPb14__Q')

# LOGGER
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello!")


#=======================================АНТИДОРОУ===============================================

# ВАРИАНТЫ
answer = ["иди нахуй", "да нахуй иди", "да, господин?", "дороу, дороу"]

# ОТВЕТ
@bot.message_handler(regexp='дороу')
#@bot.message_handler(regexp='драсти')
def otvet(message):
    msg = random.choice(answer)
#    bot.send_message(message.chat.id, msg)
    bot.reply_to(message, msg)


#========================================ПРОГНОЗ ПОГОДЫ============================================

open_weather_token = '73bfc1f783f8b62876dc954705fa8475'

#dp = Dispatcher(aiogrambot)

# /weather
#@dp.message_handler(commands=['weather'])
#async def weather_command(message: types.Message):
#    await message.reply("Че по погоде?")

#if __name__ == '__main__':
 #   executor.start_polling(dp)

# /weather
@bot.message_handler(commands=['weather'])
def weather_command(message):
    bot.send_message(message.chat.id, "Че по погоде?")

@bot.message_handler()
def get_weather(message):
#    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        bot.reply_to(message,
            f'***Погода на {date}***\n'
            f'Погода в городе: {city}\nТемпература: {cur_weather}C\nОщущается как: {feels_like}C\n'
            f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/c\n'
            f'Хорошего дня, ебать'
            )
        
#    except Exception as ex:
#        bot.reply_to(message, ' ')

bot.polling()


