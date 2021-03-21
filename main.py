import telebot
bot = telebot.TeleBot('1536625046:AAHGFNxQEvhiBICq0qoZZSCcPV5Azj8m3bs')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот, который поможет вам с опросами(голосованиями). Приятно познакомиться, {message.from_user.first_name}. Напишите команду "/help", чтобы узнать подробности работы с ботом')

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, f'Для того, чтобы создать голосование введите команду "/create"')

@bot.message_handler(commands=['create'])
def create_command(message):
    bot.reply_to(message, f'Для того, чтобы создать голосование, введите вопрос, который вас интересует')

@bot.message_handler(commands=['enough'])
def enough_command(message):
    bot.reply_to(message, f'Голосование готово')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Хорошо, теперь введите варианты ответов поочерёдно, когда ответы закончатся введите команду "/enough"')

bot.polling(none_stop=True)