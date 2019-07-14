# -*- coding: utf-8 -*-
import os
import telebot
import config
import random
import sys
import time
import psycopg2
from telebot import types
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
DATABASE_URL=os.environ['DATABASE_URL']
connect = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = connect.cursor()
#some_api_token = os.environ['SOME_API_TOKEN']
# some_api = some_api_lib.connect(some_api_token)
#              ...
bot = telebot.TeleBot(token)
mu = types.ReplyKeyboardMarkup(resize_keyboard=True)
mu.row('Еще!')
@bot.message_handler(commands=['start'])
def start_msg(message):
            bot.send_message(message.chat.id,"Привет!", reply_markup=mu)
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text="6-9", callback_data="kids")
            button1 = types.InlineKeyboardButton(text="10-13", callback_data="keys")
            button2 = types.InlineKeyboardButton(text="14-17", callback_data="keep")
            keyboard.add(button,button1,button2)
            bot.send_message(message.chat.id,"Выбери возраст!", reply_markup=keyboard)
@bot.message_handler(content_types=["text"])
def any_msg(message):
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text="6-9", callback_data="kids")
            button1 = types.InlineKeyboardButton(text="10-13", callback_data="keys")
            button2 = types.InlineKeyboardButton(text="14-17", callback_data="keep")
            keyboard.add(button,button1,button2)
            bot.send_message(message.chat.id,"Выбери возраст!", reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "kids":
            global a
            a = 1
            keyboard=types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="На взаимодействие", callback_data="inter")
            callback_button1 = types.InlineKeyboardButton(text="Уличные", callback_data="street")
            callback_button2 = types.InlineKeyboardButton(text="Шутки", callback_data="joke")
            callback_button3 = types.InlineKeyboardButton(text="На снятие напряжения", callback_data="relax")
            callback_button4 = types.InlineKeyboardButton(text="Быстрые", callback_data="quick")
            callback_button5 = types.InlineKeyboardButton(text="Тактильные", callback_data="touch")
            callback_button6 = types.InlineKeyboardButton(text="На знакомство", callback_data="know")
            keyboard.add(callback_button)
            keyboard.add(callback_button3)
            keyboard.add(callback_button1,callback_button2,callback_button4,callback_button5)
            keyboard.add(callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выбери тип игры!", reply_markup=keyboard)
        if call.data == "keys":
            a = 2
            keyboard=types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="На взаимодействие", callback_data="inter")
            callback_button1 = types.InlineKeyboardButton(text="Уличные", callback_data="street")
            callback_button2 = types.InlineKeyboardButton(text="Шутки", callback_data="joke")
            callback_button3 = types.InlineKeyboardButton(text="На снятие напряжения", callback_data="relax")
            callback_button4 = types.InlineKeyboardButton(text="Быстрые", callback_data="quick")
            callback_button5 = types.InlineKeyboardButton(text="Тактильные", callback_data="touch")
            callback_button6 = types.InlineKeyboardButton(text="На знакомство", callback_data="know")
            keyboard.add(callback_button)
            keyboard.add(callback_button3)
            keyboard.add(callback_button1,callback_button2,callback_button4,callback_button5)
            keyboard.add(callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выбери тип игры!", reply_markup=keyboard)
        if call.data == "keep":
            a = 3
            keyboard=types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="На взаимодействие", callback_data="inter")
            callback_button1 = types.InlineKeyboardButton(text="Уличные", callback_data="street")
            callback_button2 = types.InlineKeyboardButton(text="Шутки", callback_data="joke")
            callback_button3 = types.InlineKeyboardButton(text="На снятие напряжения", callback_data="relax")
            callback_button4 = types.InlineKeyboardButton(text="Быстрые", callback_data="quick")
            callback_button5 = types.InlineKeyboardButton(text="Тактильные", callback_data="touch")
            callback_button6 = types.InlineKeyboardButton(text="На знакомство", callback_data="know")
            keyboard.add(callback_button)
            keyboard.add(callback_button3)
            keyboard.add(callback_button1,callback_button2,callback_button4,callback_button5)
            keyboard.add(callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выбери тип игры!", reply_markup=keyboard)
        if call.data == "inter":
            if a == 1:
                cursor.execute("SELECT game FROM games WHERE type LIKE '%inter%' AND (age = '6-9' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                row = cursor.fetchall()
            if a == 2:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%inter%' AND (age = '10-17' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            if a == 3:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%inter%' AND (age = '10-17' OR age = '0' OR age = '14-17') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "street":
            if a == 1:
                cursor.execute("SELECT game FROM games WHERE type LIKE '%street%' AND (age = '6-9' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                row = cursor.fetchall()
            if a == 2:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%street%' AND (age = '10-17' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            if a == 3:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%street%' AND (age = '10-17' OR age = '0' OR age = '14-17') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "joke":
            if a == 1:
                cursor.execute("SELECT game FROM games WHERE type LIKE '%joke%' AND (age = '6-9' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                row = cursor.fetchall()
            if a == 2:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%joke%' AND (age = '10-17' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            if a == 3:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%joke%' AND (age = '10-17' OR age = '0' OR age = '14-17') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "relax":
            if a == 1:
                cursor.execute("SELECT game FROM games WHERE type LIKE '%relax%' AND (age = '6-9' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                row = cursor.fetchall()
            if a == 2:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%relax%' AND (age = '10-17' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            if a == 3:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%relax%' AND (age = '10-17' OR age = '0' OR age = '14-17') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "quick":
            if a == 1:
                cursor.execute("SELECT game FROM games WHERE type LIKE '%quick%' AND (age = '6-9' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                row = cursor.fetchall()
            if a == 2:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%quick%' AND (age = '10-17' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            if a == 3:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%quick%' AND (age = '10-17' OR age = '0' OR age = '14-17') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "touch":
            if a == 1:
                cursor.execute("SELECT game FROM games WHERE type LIKE '%touch%' AND (age = '6-9' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                row = cursor.fetchall()
            if a == 2:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%touch%' AND (age = '10-17' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            if a == 3:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%touch%' AND (age = '10-17' OR age = '0' OR age = '14-17') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "know":
            if a == 1:
                cursor.execute("SELECT game FROM games WHERE type LIKE '%know%' AND (age = '6-9' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                row = cursor.fetchall()
            if a == 2:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%know%' AND (age = '10-17' OR age = '0' OR age = '6-13') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            if a == 3:
                 cursor.execute("SELECT game FROM games WHERE type LIKE '%know%' AND (age = '10-17' OR age = '0' OR age = '14-17') ORDER BY RANDOM() LIMIT 1 ")
                 row = cursor.fetchall()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)

if __name__ == '__main__':
    bot.polling(none_stop=True)
