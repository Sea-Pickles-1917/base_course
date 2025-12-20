import matplotlib.pyplot as plt
import numpy as np


def lissajous(a, b, A=1, B=1, delta=np.pi/2):

    t = np.arange(0, 10, 0.01)
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)

    plt.plot(x, y)
    plt.grid(True)
    plt.savefig('lissajous.png')    

lissajous(1, 2)


