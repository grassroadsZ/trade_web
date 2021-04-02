from django.db import models


# Create your models here.


class StrategyBaseModels(models.Model):
    class Meta:
        db_table = "td_strategy_base"
        verbose_name = '策略基础配置'
        verbose_name_plural = verbose_name

    STRATEGY_CHOICES = (
        (1, "无限网格"),
        (2, "RSI买入"))

    strategy_id = models.AutoField(verbose_name="策略id", primary_key=True)
    strategy_name = models.CharField(verbose_name="策略名称", max_length=32, help_text="策略名称",default=None)
    # strategy = models.SmallIntegerField(choices=STRATEGY_CHOICES, verbose_name="策略(英文)", help_text="策略")
    strategy_param_list = models.TextField(verbose_name="策略参数列表", help_text="策略参数列表,以英文逗号分隔")

    def __str__(self):
        return self.strategy_name


class StrategyConfigModels(models.Model):
    class Meta:
        db_table = "td_strategy_config"
        verbose_name = '策略配置'
        verbose_name_plural = verbose_name

    strategy_config_id = models.IntegerField(verbose_name="自定义策略id", primary_key=True)
    strategy = models.ForeignKey(StrategyBaseModels, on_delete=models.CASCADE, verbose_name="基础策略")
    param_value = models.TextField(max_length=1024, verbose_name="策略参数key的具体值", help_text="策略参数key的具体值")
    user_strategy_name = models.CharField(verbose_name="自定义策略名称", help_text="自定义策略名称", max_length=64)

    def __str__(self):
        return self.user_strategy_name


class DealConfigModels(models.Model):
    class Meta:
        db_table = "td_deal_config"
        verbose_name = '交易配置'
        verbose_name_plural = verbose_name

    id = models.IntegerField(primary_key=True, verbose_name="交易对id")
    coin_type = models.CharField(max_length=12, verbose_name="交易对", help_text="交易对,如: BTCUSDT")
    strategy = models.ForeignKey(StrategyConfigModels, on_delete=models.CASCADE, verbose_name="使用的自定义策略",
                                 help_text="使用的自定义策略", )
    use = models.BooleanField(default=True, verbose_name="是否启用")

    def __str__(self):
        return self.coin_type


class OrderDetailModels(models.Model):
    class Meta:
        db_table = "td_order_detail"
        verbose_name = '订单记录'
        verbose_name_plural = verbose_name

    BUY_SELL_CHOICES = (
        ("buy", 1),
        ("sell", 2))

    coin_type = models.CharField(verbose_name="交易币对", help_text="交易币对", max_length=12)
    strategy_name = models.CharField(verbose_name="使用的自定义策略名称", help_text="使用的自定义策略名称", max_length=64)
    buy_sell = models.SmallIntegerField(choices=BUY_SELL_CHOICES, default="buy", verbose_name="方向")
    price = models.DecimalField(max_digits=16, decimal_places=4, verbose_name="单价")
    time = models.DateTimeField(auto_created=True, verbose_name="交易时间")
    status = models.BooleanField(default=False, verbose_name="是否以汇总")


class SummaryModels(models.Model):
    class Meta:
        db_table = "td_sum"
        verbose_name = '订单汇总记录'
        verbose_name_plural = verbose_name

    coin_type = models.CharField(verbose_name="交易币对", help_text="交易币对", max_length=12)
    strategy_name = models.CharField(verbose_name="使用的自定义策略名称", help_text="使用的自定义策略名称", max_length=64)
    amount = models.DecimalField(max_digits=16, decimal_places=4, verbose_name="利润")
    begin_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
