import os
import logging
import requests
import datetime
import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
#from aiogram.utils.helper import Helper, HelperMode, ListItem

#logging
logging.basicConfig(level=logging.INFO)

# BOT
bot_token = os.getenv("TELETOKEN")
open_weather_token = os.getenv("WEATHERTOKEN")
ipinfo_token = os.getenv("IPINFO_TOKEN")
bot = Bot(bot_token)
dp = Dispatcher(bot)
connect = sqlite3.connect("mycity_data.db")
cur = connect.cursor()
print("Подключен к БД")

# /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(f"Данный бот выдает погоду в любом городе.\n"
                        f"Введи текст в формате /weather *город*.\n"
                        f"Или введи /mycity *город* для установки своего дефолтного города, после чего сможешь использовать /weather"
                        )

# /help
#@dp.message_handler(commands=['help'])
#async def help_command(message: types.Message):
#    await message.reply(f"Данный бот выдает погоду в любом городе.\n"
#                        f"Введи текст в формате /weather *город*."
#                       )

# /city
@dp.message_handler(commands=['mycity'])
async def mycity(message: types.Message):
    text = message.text
    try:
        if text == "/mycity":
            cur.execute("SELECT id FROM cities WHERE id=?", (message.from_user.id,))
            #user_id = cur.rowcount
            #print('hui+'+user_id)
            if cur.fetchone() is not None:
                cur.execute("SELECT city FROM cities WHERE id=?", (message.from_user.id,))
                user_city = cur.fetchone()[0]
                await message.reply(f"Используй /mycity *city*, чтоб записать город, который хочешь запомнить. "
                                    f"Пока твой город: "+user_city)
            else:
                await message.reply(f"Используй /mycity *city*, чтоб записать город, который хочешь запомнить. "
                                    f"Пока что ты бомжара")
        else:
            command, text_without_command = text.split(None, maxsplit=1)
            cur.execute("INSERT INTO cities VALUES (?, ?)", (message.from_user.id, text_without_command))
            await message.reply('Город установлен')
    except:
        command, text_without_command = text.split(None, maxsplit=1)
        cur.execute("UPDATE cities SET city = ? WHERE id = ?", (text_without_command, message.from_user.id))
        await message.reply('Город заменен')
    connect.commit()

# /weather
@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    text = message.text
    if text == "/weather":
        cur.execute("SELECT city FROM cities WHERE id=?", (message.from_user.id, ))
#        my_city = str(cur.fetchall()).strip("[('',)]")
        my_city = cur.fetchone()[0]
        print(text+' '+my_city)
        text = '/weather '+my_city
    command, text_without_command = text.split(None, maxsplit=1)
    city_dict = {
        "спб": "Санкт-Петербург",
        "питер": "Санкт-Петербург",
        "мск": "Москва",
        "московия": "Москва",
        "нерезиновая": "Москва",
    }
    city_dicted = city_dict.get(text_without_command, text_without_command)
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
        "North": "\U00002B07 Северный",
        "North-East": "\U00002199 Северо-восточный",
        "East": "\U00002B05 Восточный",
        "South-East": "\U00002196 Юго-восточный",
        "South": "\U00002B06 Южный",
        "South-West": "\U00002197 Юго-западный",
        "West": "\U000027A1 Западный",
        "North-West": "\U00002198 Северо-западный"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city_dicted}&appid={open_weather_token}&units=metric"
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
        if ((wind_degree>=338)and(wind_degree<=360))or((wind_degree>0)and(wind_degree>=22)):
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
        date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')

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