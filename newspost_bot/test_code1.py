import os
import requests
import datetime
#import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

# BOT
bot_token = os.getenv("TEST_BOT")
bot = Bot(bot_token)
dp = Dispatcher(bot)

# /start
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply(f'Тебя приветствует бот, позволяющий создавать отложенные сообщения для твоего канала\n'
                        f'Введи /help для получения большей информации\n'
                        f'Введи /newpost для создания нового задания поста\n')

# /help
@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await message.reply()

#/newpost
@dp.message_handler(commands=['newpost'])
async def newpost_message(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    key_title_post = KeyboardButton(text='Заголовок (Не работает пока)', callback_data='title_post')
    key_text_post = KeyboardButton(text='Текст (Не работает пока)', callback_data='text_post')
    key_pic_post = KeyboardButton(text='Картинка (Не работает пока)', callback_data='pic_post')
    key_time_post = KeyboardButton(text='Когда выложить (Не работает пока)', callback_data='time_post')
    key_viewing_post = KeyboardButton(text='Посмотреть, что получилось (Не работает пока)', callback_data='viewing_post')
    key_release_post = KeyboardButton(text='Запостить (Не работает пока)', callback_data='release_post')
    key_back_post = KeyboardButton(text='Выйти из редактора (Не работает пока)', callback_data='back_post')
    keyboard.add(key_title_post, key_text_post)
    keyboard.add(key_pic_post, key_time_post)
    keyboard.add(key_viewing_post, key_release_post)
    keyboard.add(key_back_post)
#    await message.reply(message.from_user.id, text='Хорошо. Создай свой пост', reply_markup=keyboard, reply=False)
    await message.answer("Хорошо. Давай начнем!", reply_markup=keyboard)

@dp.callback_query_handler()
async def callback_title(callback_query: types.CallbackQuery):
    if callback_query.data == 'title_post':
        msg = 'Введи текст заголовка:'
#        query = update.callback_query
        await callback_query.answer(msg)


if __name__ == '__main__':
    executor.start_polling(dp)