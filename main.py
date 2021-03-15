import requests

from secret import API_KEY
import requester

SPY = requester.global_quote('SPY')

print(SPY['price'])