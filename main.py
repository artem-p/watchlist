import requests

from secret import API_KEY

r = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SPY&apikey=' + API_KEY)

print(r.json())