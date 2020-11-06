import signal
import sys
import params as p

def closing_signal(sig, frame):
    print(p.red + ('-' * 60) + p.nocol)
    print(p.green + 'Signal de fermeture recu' + p.nocol)
    print(p.green + 'Fermetures des positions au meilleur taux avant arret !' + p.nocol)
    p.stopbuy = True
    print(p.red + ('-' * 60) + p.nocol)
    for i in range(len(p.currency)):
        print(p.green + 'Fermeture du stream ' + p.currency[i] + p.nocol)
        p.trader.unsubscribe_market_data(p.currency[i])
    print(p.red + ('-' * 60) + p.nocol)
    print(p.green + 'Déconnexion du serveur FXCM' + p.nocol)
    p.trader.close()
    print(p.green + 'Déconnexion avec succes ! Fermeture de Forexito...' + p.nocol)
    print(p.red + ('-' * 60) + p.nocol)
    sys.exit(0)