import telebot

bot = telebot.TeleBot('1454594639:AAFsbdgaJ4ic4fbsVGONZ1dhxm7AXkPHxlo')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет')
keyboard1.row('Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


# @bot.message_handler(commands=['start'])
# def registration(message):
#     if message.text == '/reg':
#         bot.send_message(message.chat.id, "What is ur name?")
#

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '/reg':
        bot.send_message(message.chat.id, "What is ur name?")
        bot.register_next_step_handler(message, get_name)
    elif message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello my lord!')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'See u soon (Братишка Сисун)!')
    elif message.text.lower() == 'i love u':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMfYHFQET60O_6kEMiLbZDB_J6IIyAAAgwAA8A2TxPizyP_wnefvB4E')
    else:
        bot.send_message(message.chat.id, "I don't understand u...")


def get_name(message):  # получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.chat.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    age = 0
    while age == 0:  # проверяем что возраст изменился
        if message.text.isdigit():
            age = int(message.text)
        else:
            bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
    bot.send_message(message.chat.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')
    bot.register_next_step_handler(message, resp)


def resp(message):
    ans = message.text.lower()
    if ans == 'yes' or ans == 'да':
        bot.send_message(message.chat.id, 'Congrats! U have been registered!')
    elif ans == 'no' or ans == 'нет':
        bot.send_message(message.chat.id, "Pls write '/reg' again ")


@bot.message_handler(content_types=['sticker'])
def determine_stick(message):
    if message.file_id == 'CAACAgIAAxkBAAMfYHFQET60O_6kEMiLbZDB_J6IIyAAAgwAA8A2TxPizyP_wnefvB4E':
        bot.send_message(message.chat.id, 'Me too!')
        print(message)


bot.polling()
