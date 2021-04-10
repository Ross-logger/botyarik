import telebot
import PIL
from PIL import Image
from requests import get

bot = telebot.TeleBot('1454594639:AAFsbdgaJ4ic4fbsVGONZ1dhxm7AXkPHxlo')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет')
keyboard1.row('Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello my lord!')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'See u soon (Братишка Сисун)!')
    elif message.text.lower() == 'i love u':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMfYHFQET60O_6kEMiLbZDB_J6IIyAAAgwAA8A2TxPizyP_wnefvB4E')


@bot.message_handler(content_types=['sticker'])
def determine_stick(message):
    if message.file_id == 'CAACAgIAAxkBAAMfYHFQET60O_6kEMiLbZDB_J6IIyAAAgwAA8A2TxPizyP_wnefvB4E':
        bot.send_message(message.chat.id, 'Me too!')
        print(message)


bot.polling()
