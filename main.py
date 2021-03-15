import requests
from telegram.ext import Updater, CommandHandler
import logging

from secret import API_KEY, TOKEN
import requester

SPY = requester.global_quote('SPY')

print(SPY['price'])

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=SPY['price'])

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
