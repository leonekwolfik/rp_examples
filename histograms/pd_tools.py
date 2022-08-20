import numpy as np
import pandas as pd

data = np.random.choice(np.arange(10), size=10000, p=np.linspace(1, 11, 10)/60)
s = pd.Series(data)

print(s.value_counts(normalize=True).head())


ages = pd.Series(
    [1, 1, 3, 5, 8, 10 ,12, 15, 18, 18, 19, 20, 25, 30, 40, 51, 52]
)
bins = [0, 10, 13, 18, 21, np.inf]
labels = ['child', 'preteen', 'teen', 'military age', 'adult']
groups = pd.cut(ages, bins=bins, labels=labels)
print(groups.value_counts())
