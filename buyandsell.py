import params as p
import update as up
import init_ai as ini

def buy(currency, iterator, type_buy):
    ini.reinit()
    opened = p.trader.open_trade(symbol=currency, is_buy=type_buy, amount=p.amount, time_in_force='GTC', order_type='AtMarket', is_in_pips=True)
    print(p.green + ('-' * 26) + 'BUYING' + ('-' * 27) + p.nocol)
    print(p.green + 'CURRENCY: ' + str(opened.get_currency()) + p.nocol)
    print(p.green + 'QUANTITY: ' + str(opened.get_amount()) + p.nocol)
    actual = p.trader.get_last_price(currency)
    if opened.get_isBuy() == True:
        print(p.green + 'TYPE: B' + p.nocol)
        print(p.green + 'PRICE: ' + str(opened.get_buy()) + p.nocol)
        p.stop_loss[iterator] = actual['Bid'] - p.tralling
    else:
        print(p.green + 'TYPE: S' + p.nocol)
        print(p.green + 'PRICE: ' + str(opened.get_sell()) + p.nocol)
        p.stop_loss[iterator] = actual['Bid'] + p.tralling
    print(p.green + ('-' * 60) + p.nocol)
    p.buy_order[iterator] = -1
    up.update_positions()

def sell(currency, iterator):
    ini.reinit()
    p.trader.close_trade(trade_id=p.positions[iterator][0]['tradeId'], amount=p.positions[iterator][0]['amountK'])
    stk = p.positions[iterator][0]
    print(p.green + ('-' * 26) + 'CLOSING' + ('-' * 26) + p.nocol)
    print(p.green + 'CURRENCY: ' + str(stk['currency']) + p.nocol)
    print(p.green + 'QUANTITY: ' + str(stk['amountK']) + p.nocol)
    print(p.green + 'WIN/LOSS: ' + str(stk['grossPL']) + p.nocol)
    print(p.green + 'PIPS: ' + str(stk['visiblePL']) + p.nocol)
    print(p.green + ('-' * 60) + p.nocol)
    p.stop_loss[iterator] = -1
    up.update_positions()