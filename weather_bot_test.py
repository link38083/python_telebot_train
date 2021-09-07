import os
import requests
import datetime
#import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
#from aiogram.utils.helper import Helper, HelperMode, ListItem

# BOT
bot_token = os.getenv("TELETOKEN")
open_weather_token = os.getenv("WEATHERTOKEN")
bot = Bot(bot_token)
dp = Dispatcher(bot)

# /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hello!")

# /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("Данный бот выдает погоду в любом городе.\n"
                        "Введи текст в формате /weather *город*."
        )

# /weather
@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    text = message.text
    command, text_without_command = text.split(None, maxsplit=1)
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={text_without_command}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']/1.333
        wind = data['wind']['speed']
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        return await message.reply(
            f'***Погода на {date}***\n'
            f'Погода в городе: {city}\nТемпература: {cur_weather}C\nОщущается как: {feels_like}C\n'
            f'Влажность: {humidity}%\nДавление: {pressure:.2f} мм.рт.ст.\nВетер: {wind} м/c\n'
            f'Хорошего дня, ебать'
        )
    except Exception as ex:
        return await message.reply('Городом ошибся')
    except NotEnoughValues:
        return await message.reply('Введи /weather город')

if __name__ == '__main__':
    executor.start_polling(dp)