import requests
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

from secret import API_KEY, TOKEN
import requester
import plotly.graph_objects as graph_objects


def format_quote(quote):
    symbol = None
    price = None
    change = None
    change_percent = None

    if 'symbol' in quote:
        symbol = quote['symbol']
    
    if 'price' in quote:
        price = '{0:.2f}'.format(float(quote['price']))
    
    if 'change' in quote:
        change = '{0:.2f}'.format(float(quote['change']))
    
    if 'change_percent' in quote:
        change_percent = '{0:.2f}'.format(float(quote['change_percent'][:-1]))

    return {'symbol': symbol, 'price': price, 'change': change, 'change_percent': change_percent} 


def get_single_quote_text(quote):
    formatted_quote = format_quote(quote)

    return f"{formatted_quote['symbol']}: {formatted_quote['price']} {formatted_quote['change']} {formatted_quote['change_percent']}%"



SPY = requester.global_quote('SPY')
QQQ = requester.global_quote('QQQ')

spy_text = get_single_quote_text(SPY)
qqq_text = get_single_quote_text(QQQ)

output_text = f"""
{spy_text}
{qqq_text}
"""
print(output_text)


fig = graph_objects.Figure(data=[graph_objects.Table(header=dict(values=['A Scores', 'B Scores']),
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                     ])

fig.write_image('output.png', width=1000, height=1000, scale=2)


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
