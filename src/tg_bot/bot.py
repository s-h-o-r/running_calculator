import telebot
import os

def create_bot():
    token = os.getenv('TG_BOT_TOKEN')
    if not token:
        raise RuntimeError('TG_BOT_TOKEN is not set')
    return telebot.TeleBot(token)