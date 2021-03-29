import requests
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

from secret import API_KEY, TOKEN
import requester


def get_single_quote_text(quote):
    symbol = None
    price = None
    if 'symbol' in quote:
        symbol = quote['symbol']
    
    if 'price' in quote:
        price = '{0:.2f}'.format(float(quote['price']))
    
    return f"{symbol}: {price}"

SPY = requester.global_quote('SPY')
QQQ = requester.global_quote('QQQ')

spy_text = get_single_quote_text(SPY)
qqq_text = get_single_quote_text(QQQ)

output_text = f"""
{spy_text}
{qqq_text}
"""
print(output_text)



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=spy_text)

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

dispatcher.bot.send_message(chat_id='@marketwatchdaily', text=output_text)

# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

# updater.start_polling()
# updater.idle()
