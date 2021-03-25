import requests
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

from secret import API_KEY, TOKEN
import requester

def get_single_quote_text(quote):
    symbol = quote['symbol']
    price = quote['price'].strip('0')
    
    return f"{symbol}: {price}"


SPY = requester.global_quote('SPY')
QQQ = requester.global_quote('QQQ')

spy_text = get_single_quote_text(SPY)
print(spy_text)



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=spy_text)

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

dispatcher.bot.send_message(chat_id='@marketwatchdaily', text=spy_text)

# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

# updater.start_polling()
# updater.idle()
