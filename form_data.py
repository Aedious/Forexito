import params as p

# def format_last_doji(iterator, time):
#     # candle = p.data_currency[iterator][time].tail(1)
#     candle = p.data_currency[iterator].rename({'bidopen':'open', 'bidclose':'close', 'bidhigh':'high', 'bidlow':'low'}, axis='columns')
#     return candle