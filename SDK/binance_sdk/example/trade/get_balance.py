from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
g_api_key="64Y2MU90v0VYnC88tlwdd1IbDXQvnKM31dyM6amkMK7ONFh8KSYaNmM0zYAJHuDL"
g_secret_key="4VeNzAYiFHbllar77jwlmQ2dVQmLaZO2wcw9J2fNKDMzLczwqU2y5UNaSCsUCrvi"
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_balance()
PrintMix.print_data(result)
