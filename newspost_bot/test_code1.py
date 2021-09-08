import os
import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.types import KeyboardButton
from post_state import Post

#logging
logging.basicConfig(level=logging.INFO)

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
    key_back_post = KeyboardButton(text='Выйти из редактора (Не работает пока)', callback_data='exit_post')
    keyboard.add(key_title_post, key_text_post)
    keyboard.add(key_pic_post, key_time_post)
    keyboard.add(key_viewing_post, key_release_post)
    keyboard.add(key_back_post)
#    await message.reply(message.from_user.id, text='Хорошо. Создай свой пост', reply_markup=keyboard, reply=False)
    await message.answer("Хорошо. Давай начнем!", reply_markup=keyboard)

#### TITLE ####
@dp.callback_query_handler(text="title_post")
async def callback_title(callback_query: types.CallbackQuery):
    msg = 'Введи текст заголовка'
    await callback_query.answer(cache_time=20)
    logging.info(f"call = {callback_query.data}")
    await callback_query.message.answer(msg, reply=False)
    await Post.title.set()
@dp.message_handler(state=Post.title)
async def title_post(message: types.Message, state: FSMContext):
    answer = message.text
    await Post.update_data(title_post=answer)

@dp.callback_query_handler(text="text_post")
async def callback_text(callback_query: types.CallbackQuery):
    msg = 'Введи основной текст поста'
    await callback_query.answer(cache_time=20)
    logging.info(f"call = {callback_query.data}")
    await callback_query.message.answer(msg, reply=False)

@dp.callback_query_handler(text="pic_post")
async def callback_pic(callback_query: types.CallbackQuery):
    msg = 'Вставь картинку, если нужно'
    await callback_query.answer(cache_time=20)
    logging.info(f"call = {callback_query.data}")
    await callback_query.message.answer(msg, reply=False)

@dp.callback_query_handler(text="time_post")
async def callback_time(callback_query: types.CallbackQuery):
    msg = 'Введи дату в формате дд/мм/гггг чч:мм'
    await callback_query.answer(cache_time=20)
    logging.info(f"call = {callback_query.data}")
    await callback_query.message.answer(msg, reply=False)

@dp.callback_query_handler(text="exit_post")
async def callback_exit(callback_query: types.CallbackQuery):
    await callback_query.answer("Ты отменил пост", show_alert=True)
    await callback_query.message.edit_reply_markup(reply_markup=None)
    logging.info(f"call = {callback_query.data}")

if __name__ == '__main__':
    executor.start_polling(dp)