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

