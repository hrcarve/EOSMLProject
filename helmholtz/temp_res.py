import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

import helmholtz

n = 1000
den = 5e13#np.logspace(13, 14, n)
temps = np.linspace(1e10, 1.5e10, n)#p.logspace(10, 11, n)
a = 55#np.linspace(55, 65, n)
z = 28#*= 28
ye = z/a

data = pd.DataFrame(columns=list('DTYE'))

i = 0
j=0
for temp in temps:
    j+=1
    print("{} out of {}".format(j, n))
    en = int(helmholtz.helmeos(den,temp, a, z).etot)
    data.loc[i] = [den, temp, ye, en]
    i +=1
    #for temp in temps:
        #for a in a_s:
         #   en = int(helmholtz.helmeos(den, temp, a, 28).etot)
         #   data.loc[i] = [den, temp, z_s[0]/a, en]
         #   i += 1

data.to_csv(r'Temp_resolution{}_{}.csv'.format('1-1.5e10',n), index=None, header=True)
