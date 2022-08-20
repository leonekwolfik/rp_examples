import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(low=1, high=11, size=50)
y = x + np.random.randint(1, 5, size=x.size)
data = np.column_stack((x, y))

print(data)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8,4))

ax1.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
ax1.set_title('Scatter: $x$ versus $y$')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_axisbelow(True)
ax1.grid(linestyle='--')

ax2.hist(data, bins=np.arange(data.min(), data.max()), label=('x', 'y'))
ax2.legend(loc=(0))
ax2.set_title('Frequentcies of $x$ and $y$')
ax2.set_xlabel('$x$')
ax2.yaxis.tick_right()
ax2.set_axisbelow(True)
ax2.grid(linestyle='--')

plt.show()
