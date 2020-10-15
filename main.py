import telebot
from telebot import *

bot = telebot.TeleBot()

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Все про секс', 'Чи це насильство?', 'Дискримінація - що це?')
keyboard1.row('Як витрачати гроші?', 'Хочу їсти', 'Важливі контакти - звернись')
keyboard1.row('Що почитати?', 'Розваги')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привіт! Ти завітала до чат-ботині, яка відповість на будь-які твої запитання. Що тебе цікавить?',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Все про секс":
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Що це?', 'Права', 'Сексуальність')
        keyboard1.row('Поганий вплив', 'Вагітність', 'Як захиститися?')
        keyboard1.row('Куди звертатися?')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        # bot.register_next_step_handler(message, genre)





bot.polling()
