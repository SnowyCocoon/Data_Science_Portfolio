#Based on https://www.youtube.com/watch?v=_T0l015ecK4

import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2020,1,1)
end = dt.datetime(2021,1,1)

prices = web.DataReader('^NKX', 'stooq', start, end)['Close']
returns = prices.pct_change()

last_price = prices[-1]

#Numbers of simulations
num_simulations = 100
num_days = 500

simulations_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()

    price_series = []

    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 499:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulations_df[x] = price_series

fig = plt.figure()
fig.suptitle('Monte Carlo simulation: ^NKX (Nikkei 225)')
plt.plot(simulations_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Day starting from 01.01.2021')
plt.ylabel('Price in $')
plt.show()