import telebot
import os
import requests
from dotenv import load_dotenv


load_dotenv('.env.local')


TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API = os.getenv("WEATHER_API")
bot = telebot.TeleBot(TOKEN)


def api_req():
    response = requests.get('http://api.weatherapi.com/v1/current.json?key=' + WEATHER_API + '&q=Novokuznetsk')
    req = str(response.text)
    req = req.replace('"', '')
    lst = req.split(',')
    for i in range(len(lst)):
        lst[i] = lst[i].split(':')

    city = lst[0][2]
    temp = lst[10][1]
    wind = lst[15][1]
    humidity = lst[20][1]
    feelslike = lst[22][1]
    stash = [city, temp, wind, humidity, feelslike]
    return stash


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Начинаем")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    req = api_req()
    response = ['Город: ' + req[0] + '\nТемпература: ' + req[1] + '°C ' + '\nОщущается как: ' + req[4] + '°C' +
    '\nВлажность: ' + req[3] + '%' + '\nВетер: ' + req[2] + 'км/ч']
    bot.reply_to(message, response)


bot.infinity_polling()
