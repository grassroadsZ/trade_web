import ccxt


from trade_web.settings import BASE_DIR

exchange = ccxt.binance()

# 获取现货最新价格
# print(exchange.public_get_ticker_price(params={"symbol": "BTCUSDT"}))
import django
import os,sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","trade_web.settings")
django.setup()

# sys.path.append(os.path.join(BASE_DIR,os.pardir))
from trade import models

print(models.DealConfigModels.objects.all())
exit()