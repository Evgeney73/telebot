
import gspread
import telebot;
from telebot import types

gc = gspread.service_account(filename='tg-bot-398812-4af276849a6b.json')

sh = gc.open('tgb')



bot = telebot.TeleBot('6355296580:AAHSbExSPdDhJfyIxYd7we_fxbJMSq9gG_k')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Test')
    btn2 = types.KeyboardButton('Расписание уроков')
    btn3 = types.KeyboardButton('Расписание звонков')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот который поможет тебе с расписанием".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    sh = gc.open('tgb')
    a = str(sh.sheet1.get('A5:C7'))

    if (message.text == 'Расписание уроков'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="На какой день?", reply_markup=markup)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Test')
        btn2 = types.KeyboardButton('Расписание уроков')
        btn3 = types.KeyboardButton('Расписание звонков')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == 'Расписание звонков'):
        bot.send_message(message.chat.id, 'Разговор о важном - понедельник \nКлассный час - пятница \n'
                                          '8:30 - 9:10 \n1 ур. - 9:20-10:00 \n2 ур. - 10:20 - 11:00 \n'
                                          '3 ур. - 11:20 - 12:00 \n4 ур. - 12:10 - 12:50 \n5 ур. - 13:00 - 13:40 \n'
                                          '6 ур. - 13:50 - 14:30 \n7 ур. - (14:40 - 15:20)')

    elif(message.text == 'Test'):
        bot.send_message(message.chat.id, a)
    elif(message.text == 'Понедельник'):
        bot.send_message(message.chat.id, '1 ур. - 5б (8:30 - 9:10) \n2 ур. - Окно (9:20-10:00)'
                                          '\n3 ур. - 6и (10:20 - 11:00) \n4 ур. - 5г (11:20 - 12:00)'
                                          '\n5 ур. - 6к (12:10 - 12:50) \n6 ур. - 5в (13:00 - 13:40)'
                                          '\n7 ур. - 5б (13:50 - 14:30')
    elif (message.text == 'Вторник'):
        bot.send_message(message.chat.id, '1 ур. - 5в (8:30 - 9:10) \n2 ур. - 6и (9:20-10:00)'
                                          '\n3 ур. - 5г (10:20 - 11:00) \n4 ур. - 6к (11:20 - 12:00)'
                                          '\n5 ур. - 5б (12:10 - 12:50)')

    elif (message.text == 'Среда'):
        bot.send_message(message.chat.id, '1 ур. - Окно (8:30 - 9:10) \n2 ур. - 5г (9:20-10:00)'
                                          '\n3 ур. - 6и (10:20 - 11:00) \n4 ур. - 5в (11:20 - 12:00)'
                                          '\n5 ур. - 5б (12:10 - 12:50) \n6 ур. - 6к (12:10 - 12:50)')

    elif (message.text == 'Четверг'):
        bot.send_message(message.chat.id, '1 ур. - 5б (8:30 - 9:10) \n2 ур. - 6к (9:20-10:00)'
                                          '\n3 ур. - 5в (10:20 - 11:00) \n4 ур. - 5г (11:20 - 12:00)'
                                          '\n5 ур. - 6и (12:10 - 12:50)')
    elif (message.text == 'Пятница'):
        bot.send_message(message.chat.id, '1 ур. - 5б (8:30 - 9:10) \n2 ур. - 5в (9:20-10:00)'
                                          '\n3 ур. - 5г (10:20 - 11:00) \n4 ур. - 5б (11:20 - 12:00)'
                                          '\n5 ур. - 6и (12:10 - 12:50) \n6 ур. - Окно (13:00 - 13:40)'
                                          '\n7 ур. - 6к (13:50 - 14:30)')

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Test')
        btn2 = types.KeyboardButton('Расписание уроков')
        btn3 = types.KeyboardButton('Расписание звонков')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="Ты какашка из жопы")


bot.polling(none_stop=True, interval=0)
