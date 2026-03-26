from tg_bot.bot import create_bot
from tg_bot.tg_handlers import register_handlers

def main():
    bot = create_bot()
    register_handlers(bot)
    bot.infinity_polling()

if __name__ == '__main__':
    main()