import telebot

TOKEN = "6299616316:AAH8mMInznKttfbCZsEyTPmLGpyCIJ6-EQ0"

bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар' : 'USD',
    'рубль' : 'RUB',
    'евро' : 'EUR',
}

from telebot import TeleBot, types

bot = TeleBot(TOKEN)



@bot.message_handler(commands=["help"])
def help_(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("Курсы валют к рублю", "Моя VK страница")
    bot.send_message(message.chat.id, "Нажмите кнопку с нужной вам функцией", reply_markup=markup)
    bot.register_next_step_handler(message, get_curency_and_vk_link)


def get_curency_and_vk_link(message: types.Message):
    if message.text == "Курсы валют к рублю":
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.add("Показать основные валюты", "Показать все доступные валюты")
        bot.send_message(message.chat.id, "Введите индекс валюты", reply_markup=markup)
        bot.register_next_step_handler(message, show_general_currency)
    if message.text == "Курсы валют к рублю":
        ...
    else:
        bot.register_next_step_handler(message, get_curency_and_vk_link)


def show_general_currency(message: types.Message):
    list_curency = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CNY', 'RUB']
    if message.text in list_curency:
        ...
    elif message.text == "Показать основные валюты":
        bot.send_message(
            chat_id=message.chat.id,
            text="Индекс Название\n"
                 "<u>USD  Доллар США</u>\n"
                 "<u>EUR  Евро</u>\n"
                 "<u>GBP  Фунт стерлингов Великобритании</u>\n"
                 "<u>JPY  Японская йена</u>\n"
                 "<u>CHF  Швейцарский франк</u>\n"
                 "<u>CNY  Китайский юань</u>\n"
                 "<u>RUB  Российский рубль",
            parse_mode="html")
    elif message.text == "Показать все доступные валюты":
        ...
    else:
        bot.register_next_step_handler(message, show_general_currency)


if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)