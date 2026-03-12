import telebot
import os

bot = telebot.TeleBot(os.getenv('TG_BOT_TOKEN'))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Fuck yeah')

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()