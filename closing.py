import signal
import sys
import params as p

def closing_signal(sig, frame):
    if (p.quitting == False):
        p.quitting = True
        print(p.red + ('-' * 60) + p.nocol)
        print(p.green + 'Signal de fermeture recu' + p.nocol)
        rep = None
        while (rep != 'q' and rep != 'y' and rep != 'n'):
            rep = input(p.green + '[q] Pour quitter sans fermer les positions\
                \n[y] Pour quitter apres avoir fermé les positions (recommandé mais peux prendre du temps)\
                \n[n] pour annuler\nSaisissez une réponse : ' + p.nocol)
        if (rep == 'y'):
            print(p.green + 'Fermetures des positions au meilleur taux avant arret !' + p.nocol)
            p.stopbuy = True
            print(p.red + ('-' * 60) + p.nocol)
            p.quitting = False
            return
        if (rep == 'n'):
            print(p.green + 'Reprise de forexito ....' + p.nocol)
            print(p.red + ('-' * 60) + p.nocol)
            p.quitting = False
            return
        if (rep == 'q'):
            print(p.green + 'Quitter sans fermer les positions...' + p.nocol)
            print(p.red + ('-' * 60) + p.nocol)
            force_quit()

def force_quit():
    for i in range(len(p.currency)):
        print(p.green + 'Fermeture du stream ' + p.currency[i] + p.nocol)
        p.trader.unsubscribe_market_data(p.currency[i])
    print(p.red + ('-' * 60) + p.nocol)
    print(p.green + 'Déconnexion du serveur FXCM' + p.nocol)
    p.trader.close()
    print(p.green + 'Déconnexion avec succes ! Fermeture de Forexito...' + p.nocol)
    print(p.red + ('-' * 60) + p.nocol)
    sys.exit(0)

def all_trade_closed():
    for i in range(len(p.positions)):
        if (len(p.positions[i]) != 0):
            return False
    return True