import datetime as dt
import signal
import sys
import time
import strategy.doji
import strategy.ema
import pandas as pd
import buyandsell as bs
import closing
import init_ai
import params as p
import update as up

signal.signal(signal.SIGINT, closing.closing_signal)
init_ai.init_ai()
while True:
    for i in range(len(p.currency)):
        # strategy.doji.doji(p.currency[i], i)
        strategy.ema.ema(p.currency[i], i)
    up.update_candles()