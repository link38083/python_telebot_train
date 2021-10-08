import os
import logging
import requests
import datetime
import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# logging
logging.basicConfig(level=logging.INFO)

# BOT
bot_token = os.getenv("WEATHERBOT")
open_weather_token = os.getenv("WEATHERTOKEN")
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


city_dict = {
    "spb": "Санкт-Петербург",
    "спб": "Санкт-Петербург",
    "питер": "Санкт-Петербург",
    "мск": "Москва",
    "msk": "Москва",
    "московия": "Москва",
    "нерезиновая": "Москва",
    "москва": "Москва"
}


# /city
@dp.message_handler(content_types="/mycity@watislove_weather_bot")
@dp.message_handler(commands=['mycity'])
async def mycity(message: types.Message):
    text = message.text
    try:
        if text == "/mycity" or text == "/mycity@watislove_weather_bot":
            cur.execute("SELECT id FROM cities WHERE id=?", (message.from_user.id,))
            if cur.fetchone() is not None:
                cur.execute("SELECT city FROM cities WHERE id=?", (message.from_user.id,))
                user_city = cur.fetchone()[0]
                await message.reply(f"Используй /mycity *city*, где *city* - город, который ты хочешь записать. "
                                    f"Пока твой город: " + user_city
                                    )
            else:
                await message.reply(f"Используй /mycity *city*, где *city* - город, который ты хочешь записать. "
                                    f"Пока что ты бомжара"
                                    )
        else:
            command, text_without_command = text.split(None, maxsplit=1)
            city_dicted = city_dict.get(text_without_command, text_without_command).lower()
            r = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city_dicted}&appid={open_weather_token}&units=metric"
            )
            data = r.json()
            print(message.from_user.id, city_dicted, data)
            if data['cod'] == '404' or data['cod'] == 401:
                await message.reply(f"Я не знаю такого города")
            else:
                cur.execute("INSERT INTO cities VALUES (?, ?)", (message.from_user.id, text_without_command))
                await message.reply('Город установлен')
    except:
        command, text_without_command = text.split(None, maxsplit=1)
        cur.execute("UPDATE cities SET city = ? WHERE id = ?", (text_without_command, message.from_user.id))
        await message.reply('Город заменен')
    connect.commit()


# /weather
@dp.message_handler(content_types="/weather@watislove_weather_bot")
@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    text = message.text.lower()
    if text == "/weather" or text == "/weather@watislove_weather_bot":
        cur.execute("SELECT id FROM cities WHERE id=?", (message.from_user.id,))
        if cur.fetchone() is not None:
            cur.execute("SELECT city FROM cities WHERE id=?", (message.from_user.id,))
            my_city = cur.fetchone()[0]
            #print(text + ' ' + my_city)
            text = '/weather ' + my_city
        else:
            await message.reply(f"Задай себе город через '/mycity *city*', где *city* - твой город")
            return text
    command, text_without_command = text.split(None, maxsplit=1)
    print(text)
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
        0: "\U00002B07 Северный",
        1: "\U00002199 Северо-восточный",
        2: "\U00002B05 Восточный",
        3: "\U00002196 Юго-восточный",
        4: "\U00002B06 Южный",
        5: "\U00002197 Юго-западный",
        6: "\U000027A1 Западный",
        7: "\U00002198 Северо-западный"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city_dicted}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        print(data)
        city = data['name']
        cur_weather = data['main']['temp']
        weather_desc = data['weather'][0]['main']
        if weather_desc in code_to_smile:
            wd = code_to_smile[weather_desc]
        else:
            wd = "Глянь в окно лучше"
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure'] / 1.333
        wind = data['wind']['speed']
        wind_degree = data['wind']['deg']

        print(wind_degree)
        wind_de = code_to_wind_degree[((wind_degree+22)//45 % 8)]
        date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')

        return await message.reply(
            f'***Погода на {date}***\n'
            f'Погода в городе: {city}\n{wd}\nТемпература: {cur_weather:.0f}C°\nОщущается как: {feels_like:.0f}C°\n'
            f'Влажность: {humidity}%\nДавление: {pressure:.0f} мм.рт.ст.\nВетер: {wind_de} {wind:.1f} м/c\n'
            f'Хорошего дня'
        )
    except Exception as ex:
        return await message.reply('Городом ошибся')


if __name__ == '__main__':
    executor.start_polling(dp)
