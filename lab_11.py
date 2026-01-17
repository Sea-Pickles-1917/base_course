import matplotlib.pyplot as plt
import numpy as np


def astroid(R = 3):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)

    x = R/4 * np.cos(t)**3
    y = R/4* np.sin(t)**3

    plt.plot(x, y, ls = '-', lw = 3)
    plt.axis('equal')
    plt.savefig('fig_2.png')

astroid()