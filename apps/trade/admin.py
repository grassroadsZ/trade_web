from django.contrib import admin

# Register your models here.
from .models import StrategyBaseModels

admin.site.register(StrategyBaseModels)


# next_buy_price:  币对的买入价格
# grid_sell_price:    币对的卖出价格
# step: 初始仓位,整数
# profit_ratio:   差价盈利率,0.5 代表 0.5%
# double_throw_ratio:   差价补仓率 0.5 代表 0.5%
# coin_type: 交易对,如BTCUSDT
# quantity: 每次买入数量,请填写多个,需要每次买入的数量相同的话也请填写(英文逗号分隔)  如: 1,1
# max_count: 连续买入而不卖出的最大次数,用于风控, 整数
# current_num：当前连续买入次数，用于风控,整数,当current_num 次数与max_count次数相同时，该币对会自动跳过不买入