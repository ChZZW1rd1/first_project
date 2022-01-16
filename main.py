import telebot
import os
from dotenv import load_dotenv


load_dotenv('.env.local')


TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API = os.getenv("WEATHER_API")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Начинаем")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
