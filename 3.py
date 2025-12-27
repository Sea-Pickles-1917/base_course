import matplotlib.pyplot as plt
import numpy as np


def ellipse(e, p):

    phi = np.linspace(0, 2 * np.pi, 1000)
    r = p / (1 + e * np.cos(phi))

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)
    plt.grid(True)
    plt.savefig('ellipse.png') 

ellipse(e=0.5, p=1)