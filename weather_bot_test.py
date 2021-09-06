import requests
import datetime
#import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
#from aiogram.utils.helper import Helper, HelperMode, ListItem

bot = Bot(token='1979372262:AAF9Qpx-2CY3do3iG8isMr_pTvBsnmO2qQ8')
open_weather_token = '73bfc1f783f8b62876dc954705fa8475'
dp = Dispatcher(bot)

# /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hello!")

# /weather
@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    await message.reply('Город введи')
    @dp.message_handler()
    async def get_weather(message: types.Message):
        try:
            r = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
            )
            data = r.json()

            city = data['name']
            cur_weather = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']
            date = datetime.datetime.now().strftime('%Y-%m-%d')

            await message.reply(
                f'***Погода на {date}***\n'
                f'Погода в городе: {city}\nТемпература: {cur_weather}C\nОщущается как: {feels_like}C\n'
                f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/c\n'
                f'Хорошего дня, ебать'
            )
        except Exception as ex:
            await message.reply('Городом ошибся')

if __name__ == '__main__':
    executor.start_polling(dp)