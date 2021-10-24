import fxcmpy
import params as p
import update as up
from datetime import datetime
import closing

def init_ai():
    init_msg()
    init_con()
    init_stream()
    init_trades()
    init_passed_datas()
    print(p.magenta + ('-' * 60) + p.nocol)
    print(p.magenta + '\t\t\tDEMARRAGE' + p.nocol)
    print(p.magenta + ('-' * 60) + p.nocol)
    p.quitting = False

def init_msg():
    print(p.magenta + ('-' * 60) + p.nocol)
    print(p.magenta + 'Bonjour et bienvenue dans Forexito !' + p.nocol)
    print(p.magenta + ('-' * 60) + p.nocol)

def init_con():
    print(p.green + 'Connexion aux serveurs FXCM en cours...' + p.nocol)
    p.trader = fxcmpy.fxcmpy(access_token=p.token, server='demo', log_level="error", log_file='./fxcm.cfg')
    print(p.green + 'Connexion réussie !' + p.nocol)
    print(p.yellow + ('-' * 60) + p.nocol)

def init_stream():
    for i in range(len(p.currency)):
        print(p.green + 'Connexion au stream de ' + p.currency[i] + p.nocol)
        p.trader.subscribe_market_data(p.currency[i])
    print(p.yellow + ('-' * 60) + p.nocol)

def init_trades():
    print(p.green + 'Récupération des trades en cours...' + p.nocol)
    up.update_positions()
    trade_count = 0
    for x in range(len(p.positions)):
        print(p.green + 'Trades ' + str(p.currency[x]) + ':' + p.nocol)
        for y in range(len(p.positions[x])):
            print(p.green + 'Currency: ' + str(p.positions[x][y]['currency']) + '\tIsBuy: ' + str(p.positions[x][y]['isBuy']) + '\tamountK: ' + str(p.positions[x][y]['amountK']) + p.nocol)
            trade_count += 1
        print(p.green + ('-' * 30) + p.nocol)
    print(p.green + 'Récupération des trades en terminée' + p.nocol)
    print(p.green + str(trade_count) + ' trades récupérés' + p.nocol)
    print(p.yellow + ('-' * 60) + p.nocol)
    # init_stoploss()

def init_stoploss():
    for i in range(len(p.positions)):
        if len(p.positions[i]) != 0:
            reinit()
            actual = p.trader.get_last_price(p.positions[i][0]['currency'])
            if p.positions[i][0]['isBuy'] == True:
                p.stop_loss[i] = actual['Bid'] - p.tralling
            else:
                p.stop_loss[i] = actual['Bid'] + p.tralling

def init_passed_datas():
    date = datetime.timestamp(datetime.utcnow())
    date_m1 = int(date / 60) * 60 - 60
    date_m5 = int(date / 300) * 300 - 300
    date_m15 = int(date / 900) * 900 - 900
    p.should_update.append(date_m1 + 120)
    p.should_update.append(date_m5 + 600)
    p.should_update.append(date_m15 + 1800)
    date_m1 = datetime.fromtimestamp(date_m1)
    date_m5 = datetime.fromtimestamp(date_m5)
    date_m15 = datetime.fromtimestamp(date_m15)
    for i in range(len(p.currency)):
        buff = []
        print(p.green + 'Récupération des datas ' + str(p.currency[i]) + ' en cours...' + p.nocol)
        print(p.green + 'Récupération m1' + p.nocol)
        buff.append(p.trader.get_candles(p.currency[i], period='m1', number=200, end=date_m1))
        print(p.green + 'Récupération m5' + p.nocol)
        buff.append(p.trader.get_candles(p.currency[i], period='m5', number=200, end=date_m5))
        print(p.green + 'Récupération m15' + p.nocol)
        buff.append(p.trader.get_candles(p.currency[i], period='m15', number=200, end=date_m15))
        print(p.green + ('-' * 30) + p.nocol)
        p.data_currency.append(buff)

def reinit():
    if (p.trader.is_connected() == False):
        print(p.red + ('-' * 60) + p.nocol)
        print(p.red + ('ERREUR. RECONNEXION...') + p.nocol)
        init_con()
        init_stream()
    return