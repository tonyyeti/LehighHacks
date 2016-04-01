import numpy as np
from TickerDataMiner import *

price_today = []

for i in range(len(shortterm)):
    price_today.append(shortterm[i][len(shortterm[i])-1])

stock_list = indstock

returns0 = STreturnmatrix
returns1 = LTreturnmatrix
returns = np.asmatrix(returns0)
num_stocks = returns.shape[0]

horizon = 0

