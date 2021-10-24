import params as p
import buyandsell as bs
import form_data as frm
from talib.abstract import *
import closing
import pandas as pd
import numpy
import init_ai as ini
import actions as a

def ema(currency, iterator):
    # ini.reinit()
    actual = p.trader.get_last_price(currency)
    if (len(p.positions[iterator]) > 0):
        should_sell(currency, iterator, actual)
    elif (p.stopbuy == False):
        if (p.New_Data[iterator] == True):
            buy_algo(currency, iterator)
    if (p.stopbuy == True and closing.all_trade_closed()):
        closing.force_quit()

def should_sell(currency, iterator, actual):
    EMA10 =  EMA(p.data_currency[iterator][0]['bidclose'], 10)
    EMA20 =  EMA(p.data_currency[iterator][0]['bidclose'], 20)
    EMA10 = EMA10[len(EMA10) - 1]
    EMA20 = EMA20[len(EMA20) - 1]
    if (p.positions[iterator][0]['isBuy'] == True):
        if (EMA20 > EMA10):
            bs.sell(currency, iterator)
            bs.buy(currency, iterator, False)
    else:
        if (EMA20 < EMA10):
            bs.sell(currency, iterator)
            bs.buy(currency, iterator, True)

def cross_ema(small, big):
    # print(big)
    # print(small)
    i = len(big) - 1
    if (big[i - 1] < small[i - 1] and big[i] > small[i]) or (big[i - 1] > small[i - 1] and big[i] < small[i]):
        return True
    return False
    # if (big[i] < small[i]):
    #     print('market goes up')
    # if (big[i] > small[i]):
    #     print('market goes down')

def buy_algo(currency, iterator):
    EMA10 =  EMA(p.data_currency[iterator][0]['bidclose'], 10)
    EMA20 =  EMA(p.data_currency[iterator][0]['bidclose'], 20)
    if (cross_ema(EMA10, EMA20)):
        last10 = EMA10[len(EMA10) - 1]
        last20 = EMA20[len(EMA20) - 1]
        if (last20 > last10):
            bs.buy(currency, iterator, False)
        if (last20 < last10):
            bs.buy(currency, iterator, True)
    p.New_Data[iterator] = False


#algo 
# Si EMA 10 passe au dessus de EMA 20 achat
# Si reverse changement d'ordre
# détermination de phase de range peux etre un plus
# Si EMA 20 passe au dessus de EMA 10 vente b 