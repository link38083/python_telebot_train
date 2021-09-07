import os
import time
import logging

import telebot
#from telebot import apihelper

# LOGGER
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# INIT BOT
bot = telebot.TeleBot()

# /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello!")


# Polling
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(e)
        time.sleep(15)

