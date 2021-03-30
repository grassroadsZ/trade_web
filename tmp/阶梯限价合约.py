# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 14:07
# @Author  : grassroadsZ
# @File    : 阶梯限价合约.py

# import sys
# import os
#
#
# # from SDK.binance_sdk.binance_f import RequestClient
#
# # from binance_f import RequestClient
# from SDK.binance_sdk.binance_f import RequestClient
from binance_f import RequestClient

g_api_key="64Y2MU90v0VYnC88tlwdd1IbDXQvnKM31dyM6amkMK7ONFh8KSYaNmM0zYAJHuDL"
g_secret_key="4VeNzAYiFHbllar77jwlmQ2dVQmLaZO2wcw9J2fNKDMzLczwqU2y5UNaSCsUCrvi"
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
print(request_client.get_servertime())