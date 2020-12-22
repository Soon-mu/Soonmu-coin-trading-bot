import pybithumb
import time

tickers = pybithumb.get_tickers()
'''
for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(ticker, price)
    time.sleep(1)
'''
detail = pybithumb.get_market_detail('BTC')
print(detail)

orderbook = pybithumb.get_orderbook("BTC")
print(orderbook)

for k in orderbook:
    print(k)


print(orderbook['payment_currency'])
