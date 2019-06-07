import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


import helmholtz

n = 2
dens = np.logspace(-3, 15, n)
temps = np.logspace(3, 13, n)
a_s = np.linspace(50, 75, n)
z_s = np.ones(n)#np.arange(1, 10, 512)
z_s *= 28
ye = np.divide(z_s, a_s)

data = pd.DataFrame(columns=list('xyzE'))

i = 0
j=0
for den in dens:
    j+=1
    print("{} out of {}".format(j, n))
    for temp in temps:
        for a in a_s:
            en = int(helmholtz.helmeos(den, temp, a, 28).etot)
            data.loc[i] = [den, temp, z_s[0]/a, en*(10**-10)]
            i += 1

#img = ax.scatter(xs=data['x'], ys=data['y'], zs=data['z'], c=data['E'], cmap=plt.hot())
#fig.colorbar(img)
#fig.show()
#fig.savefig('figE{}.png'.format(n), dpi=150)

#print(data)
data.to_csv(r'EnergyData{}.csv'.format(n), index=None, header=False)
