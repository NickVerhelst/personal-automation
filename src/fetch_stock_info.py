# TODO: Add optional args (to focus on given stock)
# Autogenerate graphs and some financial figures.
''' Live price of The Stock '''
from yahoo_fin import stock_info
live_price = stock_info.get_live_price("TSLA")
print(round(live_price,2)," USD")


''' Stock Price From 2019 to 2021 '''
import yfinance as yf
stockSymbol = 'TSLA'
stockData = yf.Ticker(stockSymbol)
stockDf_past_2 = stockData.history(period='5d', start='2019-1-1', end='2021-12-31')
print(stockDf_past_2)