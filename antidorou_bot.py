import os
import logging
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

#logging
logging.basicConfig(level=logging.INFO)

bot_token = os.getenv("ANTIDOROU")
bot = Bot(bot_token)
dp = Dispatcher(bot)

# ОТВЕТ
answer = ["иди нахуй", "да нахуй иди", "да, господин?", "дороу, дороу", "ты, может, закончишь уже?"]
@dp.message_handler(regexp='дороу')
@dp.message_handler(regexp='драсти')
async def otvet(message: types.Message):
    msg = random.choice(answer)
    await message.reply(msg)

if __name__ == '__main__':
    executor.start_polling(dp)