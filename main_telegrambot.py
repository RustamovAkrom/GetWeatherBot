import telebot
from config import TELEGRAM_BOT_SECRET_KEY, OPEN_WEATHER_SECRET_KEY
from main import get_weather

bot = telebot.TeleBot(token=TELEGRAM_BOT_SECRET_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom menga bironbir shaharning nomini jonat men senga osha shaharning Obu-Havosini jonataman")
    bot.register_next_step_handler(message, get_weather_data)


def get_weather_data(message):
    bot.send_message(message.chat.id, "Iltimos kuting...")
    data = get_weather(message.text.strip(), OPEN_WEATHER_SECRET_KEY)
    bot.send_message(message.chat.id, data)
    

bot.polling(none_stop=True)