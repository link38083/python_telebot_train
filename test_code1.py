import os
import requests
import datetime
#import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
#from aiogram.utils.helper import Helper, HelperMode, ListItem

# BOT
bot_token = os.getenv("TEST_BOT")
bot = Bot(bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply(Что хочешь сделать?)

if __name__ == '__main__':
    executor.start_polling(dp)