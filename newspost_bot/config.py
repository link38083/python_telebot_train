import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

# BOT
bot_token = os.getenv("TEST_BOT")
bot = Bot(bot_token)
dp = Dispatcher(bot)