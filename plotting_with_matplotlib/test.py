import numpy as np

np.random.seed(21564)

a = np.random.randint(0, 10, (3, 4))

a = np.arange(1, 4)
b = np.arange(5, 8)

print(a)
print(b)

c = np.column_stack((a, b))
print(c)

r = np.row_stack((a, b))
print(r)

print(r.T)

print(np.diag([1, ] * 4))
