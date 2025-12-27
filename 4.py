import matplotlib.pyplot as plt
import numpy as np


def func(a, b):
    y = []
    x = []
    for m in np.arange(0, 10, 0.001):
        x.append(m)
        if m < a:
            y.append(a ** 2)
        elif a <= m and m <= b:
            y.append(m ** 2)
        elif m > b:
            y.append(b ** 2)
    plt.plot(x, y)
    plt.savefig('func.png')

func(3, 7)