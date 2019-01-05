#-------------------------------------------------------------------------------
# coding: utf-8
#timetable_lp_bot
#-------------------------------------------------------------------------------

import telebot

bot = telebot.TeleBot("746494018:AAHNZRQqzub0XymUYckSdH2fc0RDN--xYus")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()