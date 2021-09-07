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
    code_to_wind_degree = {
        "North": "\U00002806 Северный",
        "North-East": "\U00002197 Северо-восточный",
        "East": "\U000027A1 Восточный",
        "South-East": "\U00002198 Юго-восточный",
        "South": "\U00002B07 Южный",
        "South-West": "\U00002199 Юго-западный",
        "West": "\U00002B05 Западный",
        "North-West": "\U00002196 Северо-западный"
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
        wind_degree = data['wind']['deg']
#        for wind_degree in code_to_wind_degree:
        if ((wind_degree>=338)and(wind_degree<=360))or((wind_degree>=0)and(wind_degree>=22)):
            wind_de = code_to_wind_degree['North']
        if (wind_degree>=23)and(wind_degree<=67):
            wind_de = code_to_wind_degree['North-East']
        if (wind_degree>=68)and(wind_degree<=112):
            wind_de = code_to_wind_degree['East']
        if (wind_degree>=113)and(wind_degree<=157):
            wind_de = code_to_wind_degree['South-East']
        if (wind_degree>=158)and(wind_degree<=202):
            wind_de = code_to_wind_degree['South']
        if (wind_degree>=203)and(wind_degree<=247):
            wind_de = code_to_wind_degree['South-West']
        if (wind_degree>=248)and(wind_degree<=292):
            wind_de = code_to_wind_degree['West']
        if (wind_degree>=293)and(wind_degree<=337):
            wind_de = code_to_wind_degree['North-West']
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        return await message.reply(
            f'***Погода на {date}***\n'
            f'Погода в городе: {city}\n{wd}\nТемпература: {cur_weather}C°\nОщущается как: {feels_like}C°\n'
            f'Влажность: {humidity}%\nДавление: {pressure:.2f} мм.рт.ст.\nВетер: {wind} м/c {wind_de}\n'
            f'Хорошего дня, ебать'
        )
    except Exception as ex:
        return await message.reply('Городом ошибся')

if __name__ == '__main__':
    executor.start_polling(dp)