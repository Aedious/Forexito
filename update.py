import params as p

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