import telebot

bot = telebot.TeleBot("5081850934:AAGgE5zIU6ib8GVpSMdUFctrK9rKtSCh5e0", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Начинаем")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
