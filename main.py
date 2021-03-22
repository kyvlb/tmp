import telebot
import os
import settings

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
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



bot.polling(none_stop=True)
