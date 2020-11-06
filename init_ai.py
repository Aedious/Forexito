import fxcmpy
import params as p
import update as up

def init_ai():
    init_msg()
    init_con()
    init_stream()
    print(p.yellow + ('-' * 60) + p.nocol)
    print(p.yellow + '\t\t\tDEMARRAGE' + p.nocol)
    print(p.yellow + ('-' * 60) + p.nocol)
    print('CANDLES M1')
    candles = p.trader.get_candles('EUR/USD', period='m1', number=200)
    print(candles)
    print('CANDLES M15')
    candles = p.trader.get_candles('EUR/USD', period='m15', number=200)
    print(candles)
    print('OPEN POSITIONS')
    up.update_positions()
    print(p.positions)

def init_msg():
    print(p.yellow + ('-' * 60) + p.nocol)
    print(p.yellow + 'Bonjour et bienvenue dans Forexito !' + p.nocol)
    print(p.yellow + ('-' * 60) + p.nocol)

def init_con():
    print(p.green + 'Connexion aux serveurs FXCM en cours...' + p.nocol)
    p.trader = fxcmpy.fxcmpy(access_token=p.token, server='demo', log_level="error", log_file=None)
    print(p.green + 'Connexion réussie !' + p.nocol)
    print(p.green + ('-' * 60) + p.nocol)

def init_stream():
    for i in range(len(p.currency)):
        print(p.green + 'Connexion au stream de ' + p.currency[i] + p.nocol)
        p.trader.subscribe_market_data(p.currency[i])