from __future__ import division
from cvxopt import solvers, matrix
import matplotlib.pyplot as plt
from TickerDataMiner1 import DataSource
from radar import *
import numpy as np

#from __future__ import division
import json
import time
import requests
import pandas as pd
import numpy as np

def calculation(a1, horizon, twname):
    stock_list = DataSource(a1, horizon)[0]
    returns = DataSource(a1, horizon)[2]
    price_raw = DataSource(a1, horizon)[1]

    price_today = []
    for i in range(len(price_raw)):
        price_today.append(price_raw[i][len(price_raw[i])-1])

    returns0 = np.asmatrix(returns)
    num_stocks = returns0.shape[0]

    solvers.options["show_progress"] = False

    def optimize_mvo(returns, target_return, short_sales=False):
        """
        Solves the MVO model:
            min x'Qx
            s.t. mu'x >= target_return
                 e'x = 1
                 {x >= 0} - Short selling constraint
        """
        means = np.mean(returns, axis=1)

        p = np.cov(returns)
        q = [0.0 for _ in range(num_stocks)]
        g = np.zeros((1, num_stocks)) + np.transpose(-1.0 * means)
        h = [-target_return]

        if not short_sales:
            g = np.concatenate((g, -np.eye(num_stocks)), axis=0)
            h = h + [0.0 for _ in range(num_stocks)]

        a = np.ones((1, num_stocks))
        b = [1.0]

        solution = solvers.qp(
            matrix(2 * p),
            matrix(q),
            matrix(g),
            matrix(h),
            matrix(a),
            matrix(b)
        )

        return solution['x']

    portfolio = np.zeros((50, num_stocks))

    for i in range(0, 50):
        target = (i+1) * 0
        result = optimize_mvo(returns0, target, short_sales=False)
        for j in range(0, len(returns)):
            portfolio[i, j] = result[j]
    #print portfolio

    p = np.cov(returns)
    volatility = []
    target_vola = target_volatility(risk_level(tweet_to_traits(twname)))

    for i in range(0, 50):
        volatility.append(portfolio[i,:].dot(p).dot(portfolio[i,:].transpose()))
    volatility = np.array(volatility)
    index = np.argmin(np.absolute(volatility - target_vola))
    print portfolio[index]

    position = []
    back_list = []

    for i in range(0, num_stocks):
        if portfolio[index, i] >= 0.0001:
            back_list.append(stock_list[i])
            position.append(float(portfolio[index, i]) )
            #* price_today[i]
    print back_list
    print position

    def pie_plot(labels, sizes):
        # The slices will be ordered and plotted counter-clockwise.
        colors = ['y', 'g', 'r','c', 'm','k','w']

        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        plt.show()
        plt.savefig('picname.png')
    pie_plot(back_list, position)

    return back_list, position

#calculation([1, 3, 4], 0, 'KingJames')