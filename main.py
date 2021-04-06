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


def get_output_text(SPY, QQQ):
    spy_text = get_single_quote_text(SPY)
    qqq_text = get_single_quote_text(QQQ)

    output_text = f"""
{spy_text}
{qqq_text}
    """
    print(output_text)

    return output_text


def send_message(output_text):
    # def start(update, context):
    #     context.bot.send_message(chat_id=update.effective_chat.id, text=text_output)

    updater = Updater(token=TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    dispatcher.bot.send_message(chat_id='@marketwatchdaily', text=text_output)


def write_image(SPY, QQQ):
    spy_formatted = format_quote(SPY)
    qqq_formatted = format_quote(QQQ)

    symbol_col = [quote['symbol'] for quote in (spy_formatted, qqq_formatted) ]
    price_col = [quote['price'] for quote in (spy_formatted, qqq_formatted)]
    change_col = [quote['change'] for quote in (spy_formatted, qqq_formatted)]
    change_percent_col = [quote['change_percent'] for quote in (spy_formatted, qqq_formatted)]

    fig = graph_objects.Figure(data=[graph_objects.Table(header=dict(values=['', 'Price', 'Change', 'Change%']),
                 cells=dict(values=[symbol_col, price_col, change_col, change_percent_col]))])

    fig.write_image('output.png', width=1000, height=1000, scale=2)

def send_image():
    updater = Updater(token=TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.bot.send_photo(chat_id='@marketwatchdaily', photo=open('output.png', 'rb'))


if __name__=='__main__':
    SPY = requester.global_quote('SPY')
    QQQ = requester.global_quote('QQQ')

    text_output = get_output_text(SPY, QQQ)


    send_message(text_output)
    
    write_image(SPY, QQQ)
    send_image()


