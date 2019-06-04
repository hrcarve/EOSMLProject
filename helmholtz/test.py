import numpy as np
import matplotlib.pyplot as plt

import helmholtz

d = np.logspace(-3, 11, 512)
t = np.logspace(3, 9, 512)

# fig, axs = plt.subplots(3)

# for t in zip(ts):

    # f = helmholtz.eosfxt(dens=d, temp=t, abar=1.0, zbar=1.0)
h = helmholtz.helmeos(dens=d, temp=t, abar=1.0, zbar=1.0)
print(len(h.etot), len(t), 512 ** 2)
    # ax.plot(d, np.abs((h.ptot - f.ptot)/f.ptot))
    # ax.set_xlabel(r'$\rho$ (g/cc)')
    # ax.set_ylabel(r'fractional difference')
    # ax.set_xscale('log')
    # ax.set_yscale('log')
    # ax.set_ylim(1e-12, 1e0)

    # logT = int(np.log10(t))
    # ax.text(1e-2, 3e-6, '$T = 10^{{{}}}$ K'.format(logT))

# fig.suptitle('Pressure difference (Timmes vs Helmholtz)')
# fig.set_size_inches(6,6)
# fig.savefig('fig1.png', dpi=150)
