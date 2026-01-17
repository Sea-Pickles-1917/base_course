import matplotlib.pyplot as plt
import numpy as np


def cicloid(R = 3):
    t = np.arange(0, 2*np.pi, 0.1)
    x = R*(t - np.sin(t))
    y = R*(1 - np.cos(t))

    plt.plot(x, y, ls = '-', lw = 3)
    plt.axis('equal')
    plt.savefig('fig_3.png')

cicloid()