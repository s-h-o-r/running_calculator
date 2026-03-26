from tg_bot.use_cases import *

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def welcome_handler(message):
        greeting_message: str = ('Привет 👋\n\n'
        'Этот бот создан специально для бегунов, которые часами перед тренировкой в манеже или на дорожке пересчитываю темп от тренера в км/ч или секунды на 200м\n\n'
        'Так что скорее вводи целевой темп и побежали 🏃\n\n'
        'Напиши /help, чтобы увидеть больше команд\n\n'
        )
        bot.reply_to(message, greeting_message)

    @bot.message_handler(commands=['help'])
    def help_handler(message):
        help_message: str = (
            '/help - если забыл(а) как пользоваться ботом\n'
            '/start - вывести приветственное сообщение\n'
            '/split - В разработке 🛠️\n'
            '\n'
            'Чтобы просто конвертировать темп в км/ч или наоборот, напиши сообщение с темпом или скоростью\n'
        )
        bot.reply_to(message, help_message)

    @bot.message_handler(func=lambda message: True)
    def message_handler(message):
        bot.reply_to(message, convert_pace_or_tempo(message.text))