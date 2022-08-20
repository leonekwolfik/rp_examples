import matplotlib.pyplot as plt
fig1, ax1 = plt.subplots()
print(id(fig1))
print(id(plt.gcf()))
fig2, ax2 = plt.subplots()
print(id(fig2) == id(plt.gcf()))
print(plt.get_fignums())

def get_all_figures():
    return [plt.figure(i) for i in plt.get_fignums()]

print(get_all_figures())


plt.close('all')
print(get_all_figures())
