import telebot

# BOT
bot = telebot.TeleBot("1979372262:AAFceT_d6UbX8A1VFPnbd_K93VNHFFXaHKM")

@bot.message_handler(commands=['plusik'])
def start_message(message):
    print(message.text)
    #bot.send_sticker(message, "CAACAgEAAxkBAAEDB_dhXe197Yek0F8Sju7kLgoV3Wau3gACAgADf3BGHAXMZNg3IivIIQQ", )
    bot.reply_to(message, "/social_rank@social_credit_control_bot")

bot.polling()