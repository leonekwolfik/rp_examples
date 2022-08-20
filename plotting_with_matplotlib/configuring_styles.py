import matplotlib.pyplot as plt

[attr for attr in dir(plt) if attr.startswith('rc')]
plt.rc('lines', linewidth=2, color='r')
plt.style.use('fivethirtyeight')