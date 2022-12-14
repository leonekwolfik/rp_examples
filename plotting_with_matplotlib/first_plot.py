import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0, 1, 0.1)
# y = np.arange(10)
# plt.title("pyplot demo")
# plt.plot(x, y)
# plt.show()

np.random.seed(444)

rng = np.arange(50)
rnd = np.random.randint(0, 10, size=(3, rng.size))
# rnd = np.row_stack((rng, rng, rng))
yrs = 1950 + rng

print(rng+rnd)

fig, ax = plt.subplots(figsize=(5,3))

ax.stackplot(yrs, rng+rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
ax.set_title('Combined debt growth over time')
ax.legend(loc='upper left')
ax.set_ylabel('Total debt')
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])

fig.tight_layout()

plt.show()
