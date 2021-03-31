from django import views
from django.shortcuts import render
from .models import DealConfigModels
# Create your views here.

class TradeViews(views.View):
    # 获取币对及交易策略
    deal_info = DealConfigModels.objects.all()
    
    # 获取交易策略的基础信息(key、value)
    for deal in deal_info:
        # todo: 根据策略执行不同的逻辑
        pass
    