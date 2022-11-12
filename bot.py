# import requests
# from bs4 import BeautifulSoup
import telebot
from telebot import types
from Mytoken import token
from utils import main

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def get_message(message):
    chat_id = message.chat.id
    pressStartButton = 'Кнопка старт'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Новости KaktusMadia')
    markup.add(btn1)
    
    bot.send_message(chat_id, text="Привет, {0.first_name}! Я тестовый бот для KaktusMadia".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala (message):
    chat_id = message.chat.id
    id_ = []
    for x in main():
        id_.append(x['id'])

    if message.text == 'Новости KaktusMadia':
        list_ = main()
        for dict_ in list_:       
            bot.send_message(chat_id, f"\n{dict_['news']}\n{dict_['image']}\n".format(message.from_user))
        bot.send_message(chat_id, 'Для подробного описания введите ID статьи!')


    elif message.text in id_:
        a = message.text
        with open('message_id.txt','w') as file:
            file.write(a)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Description')
        btn2 = types.KeyboardButton('Photo')
        back = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, "some title news you can see Description of this news and Photo", reply_markup=markup)

    elif message.text == 'Photo':
        list_ = main()
        with open('message_id.txt', 'r') as file:
            id1 = file.read()
        photo = list(filter(lambda x: id1 == x['id'], list_))[0]
        bot.send_message(chat_id, f"\n{photo['image']}\n")

    elif message.text == 'Description':
        list_ = main()
        with open('message_id.txt', 'r') as file:
            id1 = file.read()
        description = list(filter(lambda x: id1 == x['id'], list_))[0]
        bot.send_message(chat_id, f"\n{description['Description']}\n")
        

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Новости KaktusMadia')
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    # elif message.text :
            # photo = list(filter(lambda x: message.text == x['id'], list_))[0]
            # bot.send_message(chat_id, f"\n{photo['image']}\n")
        # photo = list(filter(lambda x: message.text == x['id'], list_))[0]
            

        

        
          
 
bot.polling(none_stop=True)

