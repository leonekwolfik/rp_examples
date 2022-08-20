import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

n = 10
data = np.random.randint(0, n, size=n)
inds = np.arange(n)
s = pd.Series(data, inds)

# plt.rc('lines', linewidth=2, color='r')
# plt.style.use('fivethirtyeight')

plt.show()