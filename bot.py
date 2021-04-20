from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters
)

from voice import text_to_file

token_file = open('.token', 'rt')
TOKEN = token_file.read()
token_file.close()

def start(update, context):
    update.message.reply_text(f"""Привет, {update.effective_user.first_name}!
Давайте преобразуем текст в голос!
Пришлите сюда текст и в ответ вы получите голосовое сообщение""")

def help_handler(update, context):
    help_text = """Бот конвертирует текстовое сообщение в голосовое на русском языке"""
    update.message.reply_text(help_text)

def reply(update, context):
    file_name = text_to_file(update.message.text)
    update.message.reply_voice(voice=open(file_name, "rb"))

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()
