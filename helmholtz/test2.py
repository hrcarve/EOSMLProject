import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


import helmholtz

n = 2
dens = np.logspace(-3, 11, n)
temps = np.logspace(3, 9, n)
a_s = np.linspace(50, 75, n)
z_s = np.ones(n)#np.arange(1, 10, 512)
z_s *= 28
ye = np.divide(z_s, a_s)

# d = helmholtz.helmeos(dens, temps, a_s, z_s)
# print("Vary Density:", d.etot, "Vary Temp:", t.etot, "Vary A:", a.etot, "Vary Z:", z.etot)
# print(d.etot)

data = pd.DataFrame(columns=list('xyzE'))
# ens = []
# x = []
# y = []
# z = []
i = 0
j=0
for den in dens:
    j+=1
    print("{} out of {}".format(j+1, n))
    for temp in temps:
        for a in a_s:
            # x += den
            # y += temp
            # x += z_s[0]/a
            en = int(helmholtz.helmeos(den, temp, a, 28).etot)
            data.loc[i] = [den, temp, z_s[0]/a, en]
            i += 1

            # print(ens)

# print(len(ens))
# img = ax.scatter(xs=x, ys=y, zs=z, c=ens, cmap=plt.hot())
# fig.colorbar(img)
# fig.savefig('figE2.png', dpi=150)

data.to_csv(r'EnergyData{}.csv'.format(n), index=None, header=False)
