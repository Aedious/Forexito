import params as p
import buyandsell as bs
import form_data as frm
from talib.abstract import *
import closing
import pandas as pd
import numpy
import init_ai as ini
import actions as a

def doji(currency, iterator):
    ini.reinit()
    actual = p.trader.get_last_price(currency)
    if (len(p.positions[iterator]) > 0):
        should_sell(currency, iterator, actual)
    elif (p.stopbuy == False):
        if (p.New_Data[iterator] == True):
            if (p.buy_order[iterator] != -1):
                p.buy_order[iterator] = -1
                print(p.red + ('-' * 60) + p.nocol)
                print(p.red + currency + ': Ordre annulé pas d\'opportunitée détécté' + p.nocol)
                print(p.red + ('-' * 60) + p.nocol)
            should_prepare_orders(currency, iterator)
        if (p.buy_order[iterator] != -1):
            a.buy_at_price(currency, iterator, actual)
    if (p.stopbuy == True and closing.all_trade_closed()):
        closing.force_quit()

def should_prepare_orders(currency, iterator):
    p.New_Data[iterator] = False
    value = p.data_currency[iterator][0]['bidclose'][len(p.data_currency[iterator][0]['bidclose']) - 1]
    doji = CDLDOJI(p.data_currency[iterator][0]['bidopen'], p.data_currency[iterator][0]['bidhigh'],
        p.data_currency[iterator][0]['bidlow'], p.data_currency[iterator][0]['bidclose'])
    doji = doji[len(doji) - 1]
    if (doji != 0):
        print(p.yellow + ('-' * 60) + p.nocol)
        print(p.green + currency + p.nocol)
        print(p.green + 'Doji détécté' + p.nocol)
        my_ema = EMA(p.data_currency[iterator][0]['bidclose'], 200)[199]
        if (value > my_ema):
            print(p.green + 'EMA: OK' + p.nocol)
        else:
            print(p.red + 'EMA: NOT OK ANNULATION' + p.nocol)
            print(p.yellow + ('-' * 60) + p.nocol)
            return
        if (close_from_pivot(iterator) == True):
            print(p.green + 'PIVOT: OK' + p.nocol)
            print(p.green + 'PLACING ORDER' + p.nocol)
            print(p.yellow + ('-' * 60) + p.nocol)
            pre_order(iterator)
            # p.buy_order[iterator] = p.data_currency[iterator][0]['bidclose'] + ((p.data_currency[iterator][0]['bidhigh'] - p.data_currency[iterator][0]['bidclose']) * 2 / 3)
        else:
            print(p.red + 'PIVOT: NOT OK ANNULATION' + p.nocol)
            print(p.yellow + ('-' * 60) + p.nocol)
            return
    # bs.buy(p.currency[iterator], iterator, False)
    return

def should_sell(currency, iterator, actual):
    if (p.positions[iterator][0]['isBuy'] == True):
        if (actual['Bid'] < p.stop_loss[iterator]):
            bs.sell(currency, iterator)
        if (actual['Bid'] - p.tralling > p.stop_loss[iterator]):
            p.stop_loss[iterator] = actual['Bid'] - p.tralling 
    else:
        if (actual['Bid'] > p.stop_loss[iterator]):
            bs.sell(currency, iterator)
        if (actual['Bid'] + p.tralling < p.stop_loss[iterator]):
            p.stop_loss[iterator] = actual['Bid'] + p.tralling
    return

def PivotPoints(df):  
    PP = pd.Series((df['bidhigh'] + df['bidlow'] + df['bidclose']) / 3)  
    R1 = pd.Series(2 * PP - df['bidlow'])  
    S1 = pd.Series(2 * PP - df['bidhigh'])  
    R2 = pd.Series(PP + df['bidhigh'] - df['bidlow'])  
    S2 = pd.Series(PP - df['bidhigh'] + df['bidlow'])  
    R3 = pd.Series(df['bidhigh'] + 2 * (PP - df['bidlow']))  
    S3 = pd.Series(df['bidlow'] - 2 * (df['bidhigh'] - PP))  
    psr = {'PP':PP, 'R1':R1, 'S1':S1, 'R2':R2, 'S2':S2, 'R3':R3, 'S3':S3}  
    PSR = pd.DataFrame(psr)
    PSR = PSR.iloc[len(PSR) - 1]
    return PSR

def close_from_pivot(iterator):
    pivot = PivotPoints(p.data_currency[iterator][2])
    value = p.data_currency[iterator][0]['bidclose'][len(p.data_currency[iterator][0]['bidclose']) - 1]
    idx = numpy.argmin(numpy.abs(value - pivot))
    point = 0
    compare = None
    placement = None
    value = pivot[idx]
    if (value == pivot[idx]):
        return True
    if (value < pivot[idx]):
        placement = 'neg'
        if (pivot.keys()[idx][0] == 'P'):
            compare = 'S1'
        elif (pivot.keys()[idx][0] == 'R'):
            if (pivot.keys()[idx] == 'R1'):
                compare = 'PP'
            else:
                point = int(pivot.keys()[idx][1]) - 1
                compare = 'R' + str(pivot)
        elif (pivot.keys()[idx][0] == 'S'):
            point = int(pivot.keys()[idx][1]) + 1
            if (point >= 4):
                return False
            else:
                compare = 'S' + str(point)
    else:
        placement = 'pos'
        if (pivot.keys()[idx][0] == 'P'):
            compare = 'R1'
        elif (pivot.keys()[idx][0] == 'R'):
            point = int(pivot.keys()[idx][1]) + 1
            if (point >= 4):
                return False
            else:
                compare = 'R' + str(point)
        elif (pivot.keys()[idx][0] == 'S'):
            if (pivot.keys()[idx] == 'S1'):
                compare = 'PP'
            else:
                point = int(pivot.keys()[idx][1]) - 1
                compare = 'S' + str(pivot)
    if (placement == 'neg'):
        if (value >= pivot[idx] - ((pivot[idx] - pivot[compare]) / 4)):
            return True
        else:
            return False
    else:
        if (value <= pivot[idx] + ((pivot[compare] - pivot[idx]) / 4)):
            return True
        else:
            return False
    return False

def pre_order(iterator):
    close = p.data_currency[iterator][0]['bidclose'][len(p.data_currency[iterator][0]['bidclose']) - 1]
    high = p.data_currency[iterator][0]['bidhigh'][len(p.data_currency[iterator][0]['bidhigh']) - 1]
    low = p.data_currency[iterator][0]['bidlow'][len(p.data_currency[iterator][0]['bidlow']) - 1]
    if (p.buy_order_type[iterator] == 'B'):
        diff = (high - close) / 3
        if (diff > 0.00003):
            p.buy_order[iterator] = close + diff
        else:
            p.buy_order[iterator] = close + 0.00004
    else:
        diff = (close - low) / 3
        if (diff > 0.00003):
            p.buy_order[iterator] = close - diff
        else:
            p.buy_order[iterator] = close - 0.00004

    # R3 - R2 - R1 - PP - S1 - S2 - S3