#User Params
token = ''
currency = ['EUR/USD', 'GBP/USD', 'USD/CHF', 'AUD/USD']
# currency = ['EUR/USD', 'GBP/USD', 'USD/CHF', 'AUD/USD', 'EUR/GBP', 'EUR/CHF', 'AUD/NZD', 'NZD/CAD', 'GBP/CHF', 'USD/JPY']
periods = ['m1', 'm5', 'm15']
data_currency = []
should_update = []
positions = []
buy_order = [-1, -1, -1, -1]
# buy_order = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# buy_order_type = ['B', 'B', 'B', 'B']
# buy_order_type = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
buy_order_type = ['S', 'S', 'S', 'S']
# stop_loss = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
stop_loss = [-1, -1, -1, -1]
start = [False, False, False, False]
#Global variables
trader = None
stopbuy = False
quitting = True
New_Data = [True, True, True, True]
# New_Data = [True, True, True, True, True, True, True, True, True, True]
amount = 1
# amount = 100
tralling = 0.0002

#Terminal colors
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
nocol = '\033[0m'

currency_list = [
'AUD/CAD', 'AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/USD', 'CAD/CHF', 'CAD/JPY',
'CHF/JPY', 'EUR/AUD', 'EUR/CAD', 'EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'EUR/NOK',
'EUR/NZD', 'EUR/SEK', 'EUR/TRY', 'EUR/USD', 'GBP/AUD', 'GBP/CAD', 'GBP/CHF',
'GBP/JPY', 'GBP/NZD', 'GBP/USD', 'NZD/CAD', 'NZD/CHF', 'NZD/JPY', 'NZD/USD',
'TRY/JPY', 'USD/CAD', 'USD/CNH', 'USD/HKD', 'USD/JPY', 'USD/MXN', 'USD/NOK',
'USD/SEK', 'USD/TRY', 'USD/ZAR', 'XAG/USD', 'XAU/USD', 'ZAR/JPY', 'USD/ILS',
'BTC/USD', 'BCH/USD', 'ETH/USD', 'LTC/USD', 'XRP/USD', 'EOS/USD', 'XLM/USD',
'USD/CHF'
]

# R3 - R2 - R1 - PP - S1 - S2 - S3
# S ask
# B bid