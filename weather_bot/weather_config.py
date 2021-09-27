import requests
import datetime

open_weather_token = os.getenv("WEATHERTOKEN")

def get_weather(city, open_weather_token):
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

        print(
            f'***Погода на {date}***\n'
            f'Погода в городе: {city}\nТемпература: {cur_weather}C\nОщущается как: {feels_like}C\n'
            f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/c\n'
            f'Хорошего дня, ебать'
            )
        
    except Exception as ex:
        print(ex)
        print('Проверь название')

def main():
    city = input('Введи город: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
