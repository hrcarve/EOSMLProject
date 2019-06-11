import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 5
data = pd.read_csv("EnergyData5.csv", sep=",", header=None)

img = ax.scatter(xs=data[0], ys=data[1], zs=data[2], c=data[3], cmap=plt.hot())
fig.colorbar(img)
fig.savefig('figE{}.png'.format(n), dpi=150)
