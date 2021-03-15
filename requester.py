import requests
from secret import API_KEY

def global_quote(ticker):
    query = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
    request = requests.get(query)
    return request.json()