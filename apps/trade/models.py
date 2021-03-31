from django.db import models


# Create your models here.

class DealConfigModels(models.Model):
    class Meta:
        db_table = "td_deal_config"
        verbose_name = '交易配置'
        verbose_name_plural = verbose_name

    id = models.IntegerField(primary_key=True, verbose_name="交易对id")
    coin_type = models.CharField(max_length=12, verbose_name="交易对", help_text="交易对,如: BTCUSDT")
    strategy = models.ForeignKey(verbose_name="策略", help_text="使用的策略", )

    def __str__(self):
        return self.coin_type


class StrategyBaseModels(models.Model):
    class Meta:
        db_table = "td_strategy_base"
        verbose_name = '策略基础配置'
        verbose_name_plural = verbose_name

    strategy_id = models.IntegerField(primary_key=True, verbose_name="策略id")
    coin_type = models.CharField(max_length=12, verbose_name="交易对", help_text="交易对,如: BTCUSDT")
    strategy = models.CharField(verbose_name="策略", help_text="策略")

    def __str__(self):
        return self.strategy_id


class StrategyConfigModels(models.Model):
    class Meta:
        db_table = "td_strategy_config"
        verbose_name = '策略配置'
        verbose_name_plural = verbose_name

    strategy_config_id = models.IntegerField(primary_key=True, verbose_name="具体策略id")
    strategy_key = models.ForeignKey(StrategyBaseModels, on_delete=models.CASCADE, verbose_name="策略")
    param_key = models.CharField(max_length=12, verbose_name="策略key", help_text="策略key,如: ")
    # strategy = models.ForeignKey(DealConfigModels, on_delete=models.CASCADE, verbose_name="策略", help_text="策略" )
