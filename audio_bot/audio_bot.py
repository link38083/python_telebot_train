import os
import logging
import keyboards
from keyboards import DataInput
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from vk_api.audio import VkAudio
import vk_api

# logging
logging.basicConfig(level=logging.INFO)

# BOT
def two_factor():
    code = input("Code? ")
    remember_device = True
    return code, remember_device

vk_loginn = os.getenv("vk_login")
vk_password = os.getenv("vk_pass")
vk_session = vk_api.VkApi(vk_loginn, vk_password, auth_handler=two_factor)
vk_session.auth()
vkaudio = VkAudio(vk_session)
bot_token = os.getenv("TEST_BOT")
bot = Bot(bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())

# ALBUMS


# /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f"Данный бот поможет тебе импортировать музыку между сервисами\n"
                        f"Выбери сервис из которого хочешь импортировать музыку", reply_markup=keyboards.first_keyboard)

# FROM BOOM
@dp.callback_query_handler(lambda c: c.data == "from_boom")
async def from_boom_def(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, text="Введи ссылку или id своей страницы ВК.\n"
                                                   "Убедись, что аудиозаписи открыты, иначе бот не сможет прочитать твой список аудио")
    await DataInput.vk_link.set()

@dp.message_handler(state=DataInput.vk_link)
async def vk_link(message: types.Message, state: FSMContext):
    user_id = message.text
    print(state)
    await message.answer(text = f"Окей, выбери альбом", reply_markup=keyboards.albums_keyboard)
    await state.finish()

@dp.callback_query_handler(lambda c: c.data[:6] == "album_")
async def album_get(call: types.CallbackQuery):
    print(user_id)
    print("Вызвалось")
    print(call.data)
    print(call.data[6:])
    await bot.answer_callback_query(call.id)
    album_number = (call.data)[6:]
    tracks = []
    for track in vkaudio.get(album_id=album_number):
        tracks.append(track.get('artist')+" - "+track.get('title'))
    print(tracks)
    await bot.send_message(call.from_user.id, text=tracks)

# FROM YAMUSIC
@dp.callback_query_handler(lambda c: c.data == "from_yamusic")
async def from_boom_def(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, text="Введи ссылку на плейлист.\n")



if __name__ == '__main__':
    executor.start_polling(dp)
    #print("--- %s seconds ---" % (time.time() - start))
