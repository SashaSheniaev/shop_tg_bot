import telebot
from telebot import types
import random
import time

TOKEN = '7616629906:AAE0hFK_I0G5_NYbg2hvdm82kuWCKJWexlE'
bot = telebot.TeleBot(TOKEN)

products = []
cart = {}
returns = []

def get_main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        types.KeyboardButton('Команди'),
        types.KeyboardButton('Додати товар'),
        types.KeyboardButton('Товари'),
        types.KeyboardButton('Кошик'),
        types.KeyboardButton('Оплата'),
        types.KeyboardButton('Повернути товар'),
    )
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "Вітаємо у боті!\n\n"
        "Використовуйте кнопки нижче для роботи з ботом.\n\n"
        "Доступні команди:\n"
        "Команди\n"
        "Додати товар\n"
        "Товари\n"
        "Кошик\n"
        "Оплатити\n"
        "Повернути товар"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_keyboard())
@bot.message_handler(commands=['add_products'])
def add_products(message):
    msg = bot.send_message(message.chat.id, "Введіть назву товару, який хочете додати:", reply_markup=get_main_keyboard())
    bot.register_next_step_handler(msg, process_product_name)



