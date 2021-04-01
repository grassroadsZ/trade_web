from django import views

from .models import DealConfigModels, StrategyConfigModels


# Create your views here.

class TradeViews(views.View):

    def get_func_param_value(self):
        # 获取币对及自定义交易策略 [{"ethusdt","定投策略"},{"ethusdt","倍投策略"}]
        deal_lists: list(dict) = [{i.coin_type: i.strategy} for i in DealConfigModels.objects.all()]

        # 获取自定义策略对应的基础策略及参数key和value
        new_deal_lists = {}
        for deal in deal_lists:
            for k, v in deal.items():
                # {"xrp+自定义策略1"：{基础策略:{key:value}}}
                new_deal_lists[k + v] = {i.strategy_key: {i.param_key: i.param_value} for i in
                                         StrategyConfigModels.objects.filter(user_strategy_name=v)}

        return new_deal_lists

    def unlimited_grid(self, **kwargs):

        cur_market_price = exchange.get_ticker_price(params={"symbol": kwargs.get("coin_type")})  # 当前交易对市价
        buy_price = kwargs.get("next_buy_price")  # 当前网格买入价格
        sell_price = kwargs.get("grid_sell_price")  # 当前网格卖出价格
        # quantity = self.get_quantity(kwargs.get()
        step = kwargs.get("step")  # 当前步数
        current_num = kwargs.get("current_num")  # 当前连续买入次数
        max_count = kwargs.get("max_count")  # 连续买入而不卖出的最大次数

        if buy_price >= cur_market_price:
            pass
