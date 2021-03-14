import yfinance as yf

msft = yf.Ticker('AAPL')

info = msft.info

print(info)