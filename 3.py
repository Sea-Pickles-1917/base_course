import matplotlib.pyplot as plt
import numpy as np


def ellipse(e, p):

    phi = np.linspace(0, 2 * np.pi, 1000)
    r = p / (1 + e * np.cos(phi))

    plt.plot(phi, r)
    plt.grid(True)
    plt.savefig('ellipse.png') 

ellipse(e=-2, p=1)