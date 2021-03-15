import requests
from secret import API_KEY

def global_quote(ticker):
    quote = {}

    query = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
    request = requests.get(query)

    if request.status_code == 200:
        quote['price'] = request.json()['Global Quote']['05. price']

    return quote