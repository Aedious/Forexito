import params as p
from datetime import datetime
import init_ai as ini

def update_positions():
    p.positions = []
    positions = p.trader.get_open_positions(kind='list')
    sort = []
    buff = []
    for i in range(len(p.currency)):
        for x in range(len(positions)):
            if (positions[x]['currency'] == p.currency[i]):
                buff.append(positions[x])
        sort.append(buff)
        buff = []
    p.positions = sort

def update_candles():
    date = datetime.timestamp(datetime.utcnow())
    ini.reinit()
    for x in range(len(p.data_currency)):
        for y in range(len(p.data_currency[x])):
            if (y == 0 and date >= p.should_update[y]):
                p.data_currency[x][y] = p.trader.get_candles(p.currency[x], period='m1', number=200, end=datetime.fromtimestamp(int(date / 60) * 60 - 60))
            if (y == 1 and date >= p.should_update[y]):
                p.data_currency[x][y] = p.trader.get_candles(p.currency[x], period='m5', number=200, end=datetime.fromtimestamp(int(date / 300) * 300 - 300))
            if (y == 2 and date >= p.should_update[y]):
                p.data_currency[x][y] = p.trader.get_candles(p.currency[x], period='m15', number=200, end=datetime.fromtimestamp(int(date / 900) * 900 - 900))
    up = False
    if (date >= p.should_update[0]):
        print(p.yellow + ('-' * 60) + p.nocol)
    if (date >= p.should_update[2]):
        p.should_update[0] = int(date / 60) * 60 + 60
        p.should_update[1] = int(date / 300) * 300 + 300
        p.should_update[2] = int(date / 900) * 900 + 900
        print(p.yellow + 'UPDATE M1/M5/M15' + p.nocol)
        up = True
    elif (date >= p.should_update[1]):
        p.should_update[0] = int(date / 60) * 60 + 60
        p.should_update[1] = int(date / 300) * 300 + 300
        print(p.yellow + 'UPDATE M1/M5' + p.nocol)
        up = True
    elif (date >= p.should_update[0]):
        p.should_update[0] = int(date / 60) * 60 + 60
        print(p.yellow + 'UPDATE M1' + p.nocol)
        up = True
    if up == True:
        print(p.yellow + ('-' * 60) + p.nocol)
        for i in range( len(p.New_Data) ):
            p.New_Data[i] = True