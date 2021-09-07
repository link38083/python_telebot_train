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
    await message.reply(f"Данный бот выдает погоду в любом городе.\n"
                        f"Введи текст в формате /weather *город*."
                       )

# /weather
@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    text = message.text
    command, text_without_command = text.split(None, maxsplit=1)
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={text_without_command}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        weather_desc = data['weather'][0]['main']
        if weather_desc in code_to_smile:
            wd = code_to_smile[weather_desc]
        else:
            wd = "Глянь в окно лучше"
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']/1.333
        wind = data['wind']['speed']
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        return await message.reply(
            f'***Погода на {date}***\n'
            f'Погода в городе: {city}\n{wd}\nТемпература: {cur_weather}C°\nОщущается как: {feels_like}C°\n'
            f'Влажность: {humidity}%\nДавление: {pressure:.2f} мм.рт.ст.\nВетер: {wind} м/c\n'
            f'Хорошего дня, ебать'
        )
    except Exception as ex:
        return await message.reply('Городом ошибся')

if __name__ == '__main__':
    executor.start_polling(dp)