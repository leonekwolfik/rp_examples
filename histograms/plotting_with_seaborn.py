import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


np.random.seed(444)

d = np.random.laplace(loc=15, scale=3, size=500)

sns.set_style('darkgrid')
sns.distplot(d, fit=stats.laplace, kde=False)

plt.show()
