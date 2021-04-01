import ccxt

exchange = ccxt.binance()




class Strategy(object):

    @staticmethod
    def unlimited_grid(**kwargs):
        cur_market_price = exchange.get_ticker_price(params={"symbol": kwargs.get("coin_type")})  # 当前交易对市价
        buy_price = kwargs.get("next_buy_price")  # 当前网格买入价格
        sell_price = kwargs.get("grid_sell_price")  # 当前网格卖出价格
        # quantity = self.get_quantity(kwargs.get()
        step = kwargs.get("step")  # 当前步数
        current_num = kwargs.get("current_num")  # 当前连续买入次数
        max_count = kwargs.get("max_count")  # 连续买入而不卖出的最大次数
        
        if buy_price >= cur_market_price:
            pass
            
