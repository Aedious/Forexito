import datetime as dt
import params as p
import init_ai
import pandas as pd
import signal
import sys
import closing
import time

signal.signal(signal.SIGINT, closing.closing_signal)
#SUBSCRIBE TO ALL CURRENCIES BEFORE GET LIVE DATA
init_ai.init_ai()

#INIT ALL PROCESSES FUNCTION REQUIRED

p.trader.subscribe_market_data('EUR/USD')
p.trader.get_subscribed_symbols()
actual = p.trader.get_last_price('EUR/USD')
while True:
    # actual = p.trader.get_prices('EUR/USD')
    actual = p.trader.get_last_price('EUR/USD')
    print(actual)
    time.sleep(2)
print(p.trader)
print('logged')
# p.trader.open_trade(symbol=p.currency, is_buy=direction,amount=p.amount, time_in_force='GTC', order_type='AtMarket', is_in_pips=True, limit=p.limit, stop=p.stop, trailing_step=10)
# p.trader.open_trade(symbol='EUR/USD', is_buy=True,amount=1, time_in_force='GTC', order_type='AtMarket', is_in_pips=True)
# trade = trader.open_trade(symbol='EUR/USD', is_buy=True,amount=1, time_in_force='GTC', order_type='AtMarket')
print('1')
trade = p.trader.get_open_positions(kind='list')
print(trade)
print(trade[0])
print('2')
# trader.close_trade(trade_id=position['tradeId'], amount=position['amountK'])
# trader.close_trade(trade_id=trade['orderId:'])