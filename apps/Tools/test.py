import ccxt

exchange = ccxt.binance()

# 获取现货最新价格
print(exchange.public_get_ticker_price(params={"symbol": "BTCUSDT"}))

exit()