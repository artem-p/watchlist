import requests
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

from secret import API_KEY, TOKEN
import requester

SPY = requester.global_quote('SPY')

spy_price = SPY['price'].strip('0')
spy_text = f"SPY: {spy_price}"
print(spy_text)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=spy_text)

def callback_minute(context: CallbackContext):
    print('callback minute')
    context.bot.send_message(chat_id='@marketwatchdaily', text='One message every minute')

updater = Updater(token=TOKEN, use_context=True)

job_queue = updater.job_queue

job_minute = job_queue.run_repeating(callback_minute, interval=60, first=10)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()

