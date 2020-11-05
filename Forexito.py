import fxcmpy
import datetime as dt
import params
import User_inputs as imputs
import pandas as pd

#SUBSCRIBE TO ALL CURRENCIES BEFORE GET LIVE DATA
imputs.User_Imputs()
#INIT ALL PROCESSES FUNCTION REQUIRED
trader = fxcmpy.fxcmpy(access_token=params.token, log_level="error", log_file=None)
trader.subscribe_market_data('EUR/USD')
trader.get_subscribed_symbols()
actual = trader.get_last_price('EUR/USD')
while True:
    print('1')
    actual = trader.get_prices('EUR/USD')
    print(actual)
    print('2')
    actual = trader.get_last_price('EUR/USD')
    print(actual)
exit(0)
print(trader)
print('logged')
# params.trader.open_trade(symbol=params.currency, is_buy=direction,amount=params.amount, time_in_force='GTC', order_type='AtMarket', is_in_pips=True, limit=params.limit, stop=params.stop, trailing_step=10)
# params.trader.open_trade(symbol='EUR/USD', is_buy=True,amount=1, time_in_force='GTC', order_type='AtMarket', is_in_pips=True)
# trade = trader.open_trade(symbol='EUR/USD', is_buy=True,amount=1, time_in_force='GTC', order_type='AtMarket')
print('1')
trade = trader.get_open_positions(kind='list')
print(trade)
print(trade[0])
print('2')
# trader.close_trade(trade_id=position['tradeId'], amount=position['amountK'])
# trader.close_trade(trade_id=trade['orderId:'])