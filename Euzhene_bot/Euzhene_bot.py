from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os

def start(update:Update, callbackContext:CallbackContext):
    update.message.reply_text("Привет, меня зовут Ассистент Арчип. Напиши команду /help и узнай мои возможности.")

def help(update:Update, callbackContext:CallbackContext):
    update.message.reply_text(""""Доступные команды:
    /greet - поприветствовать вызвавшего
    /whoIsBoss - узнать, кто есть босс
    /releaseNews - новости обновлений
    """)

def whoIsBoss(update:Update, callbackContext:CallbackContext):
    update.message.reply_text("Женя мой босс")

def greet(update:Update, callbackContext:CallbackContext):
    update.message.reply_text("Привет, %s"%update.message.from_user.first_name)

def releaseNews(update:Update, callbackContext:CallbackContext):
    update.message.reply_text("""Версия 0.1. 
    - Добавлены простейшие функции-респонды""")

def main():
    TOKEN = "5714319791:AAHqJfa3xcoEh009YKYXSsIZ9F_SVTsFik8"
    APP_NAME = "https://euzhene-bot.herokuapp.com/"
    PORT = int(os.environ.get('PORT','8443'))
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('whoIsBoss', whoIsBoss))
    updater.dispatcher.add_handler(CommandHandler('greet', greet))
    updater.dispatcher.add_handler(CommandHandler('releaseNews', releaseNews))


    updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN,webhook_url=APP_NAME+TOKEN)

if __name__=='__main__':
    main()
