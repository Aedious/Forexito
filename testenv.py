import talib
import numpy

sample_data = [
    ['1/22/14', 10, 18,  5, 20],
    ['1/23/14', 12, 21,  7, 22],
    ['1/24/14', 14, 24, 9 , 24],
    ['1/25/14', 16, 27, 11, 26],
    ['1/26/14', 18, 30, 13, 28],
    ['1/27/14', 20, 33, 15, 30],
    ['1/28/14', 22, 36, 17, 32],
    ['1/29/14', 24, 39, 19, 34],
    ['1/30/14', 26, 41, 21, 38],
    ['1/31/14', 30, 45, 25, 40],
    ['2/01/14', 43, 44, 42, 49],
    ['2/02/14', 45, 45, 45, 45],
    ['2/03/14', 44, 45, 43, 47],
    ['2/04/14', 40, 55, 35, 50],
]

# convert data to columns
sample_data = numpy.column_stack(sample_data)

# extract the columns we need, making sure to make them 64-bit floats
open = sample_data[1].astype(float)
print(min(open))
high = sample_data[2].astype(float)
low = sample_data[3].astype(float)
close = sample_data[4].astype(float)
# index = 0
# stk = None
# truc = 18.5
# for (i in range(len(sample_data))):
#     if (stk == None):
#         stk = abs()
idx = numpy.argmin(numpy.abs(29 - open))
print(idx)
print(open[idx])
print(talib.CDLDOJI(open, high, low, close))
print(talib.CDLMORNINGDOJISTAR(open, high, low, close))
print(talib.CDLDOJISTAR(open, high, low, close))
print(talib.CDLDRAGONFLYDOJI(open, high, low, close))
print(talib.CDLEVENINGDOJISTAR(open, high, low, close))
print(talib.CDLGRAVESTONEDOJI(open, high, low, close))
print(talib.CDLLONGLEGGEDDOJI(open, high, low, close))