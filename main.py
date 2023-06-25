import telebot
import requests
import json

TOKEN = "6299616316:AAH8mMInznKttfbCZsEyTPmLGpyCIJ6-EQ0"
headers= {
  "apikey": "3Jlw0SOoB4pHayS2NY1OnDLmaIgshLY7"
}

bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар' : 'USD',
    'рубль' : 'RUB',
    'евро' : 'EUR',
}

class CovertionException(Exception):
    pass


from telebot import TeleBot, types

bot = TeleBot(TOKEN)



@bot.message_handler(commands=["help", "start"])
def help_(message: types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(commands=["values", ])
def help_(message: types.Message):
    bot.send_message(message.chat.id, "Доступная Валюта: \nДоллар\nРубль\nЕвро")

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    if len(values) > 3:
        raise CovertionException('Слишком много параметров')
    quote, base, amount = values
    if quote == base:
        raise CovertionException(f'Невозможно перевести одинаковые валюты {base}')
    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise CovertionException(f'Не удалось обработать валюту {quote}')
    try:
        base_ticker = keys[base]
    except KeyError:
        raise CovertionException(f'Не удалось обработать валюту {base}')

    try:
        amount = float(amount)
    except ValueError:
        raise CovertionException(f'Не удалось обработать колличество {amount}')

    r = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}', headers=headers)
    total_base = json.loads(r.content)['result']
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)

bot.polling(skip_pending=True)
    bot.infinity_polling(skip_pending=True)
