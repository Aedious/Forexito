#User Params
token = 'fd9ac39beb84d3114e6c61d3fb10fb5a3b6ad116'
currency = ['EUR/USD', 'GBP/USD', 'USD/CHF', 'AUD/USD']

#Global variables
trader = None
stopbuy = False
positions = []

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

#ta-lib

# past_orders = p.trader.get_order_ids()
# candles = p.trader.get_candles('EUR/USD', period='m1', number=200)