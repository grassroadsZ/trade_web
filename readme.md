整体逻辑
1.在策略配置中根据策略基础配置来配置策略的具体值
2.在交易配置表中配置 币种 + 在1中配置的自定义策略
3.通过交易配置表，找出交易对及使用的的自定义策略
4.通过使用的自定义策略找到该自定义策略下的所有的参数key及具体的参数值及初始策略
5.将参数key及参数值传递给binance_trade 中的Strategy的初始策略进行调用