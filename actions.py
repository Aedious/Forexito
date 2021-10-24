import params as p
import buyandsell as bs

def buy_at_price(currency, iterator, actual):
    if (p.buy_order_type[iterator] == 'B'):
        if (actual['Bid'] >= p.buy_order[iterator]):
            bs.buy(p.currency[iterator], iterator, True)
    else:
        if (actual['Bid'] <= p.buy_order[iterator]):
            bs.buy(p.currency[iterator], iterator, False)