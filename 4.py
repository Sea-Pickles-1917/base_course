import matplotlib.pyplot as plt
import numpy as np


def func(a, b, x):
    x = np.arange(0 , 10, 0.001)
    if x < a:
        return a ** 2
    elif a <= x and x <= b:
        return x ** 2
    elif x > b:
        return b ** 2
    
    x = np.linspace(-5, 10, 500)
    y = func(a, b, x)

    plt.plot(x, y)
    plt.grid(True)
    plt.savefig('func.png')

func(1, 5, 7)