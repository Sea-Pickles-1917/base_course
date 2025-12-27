import matplotlib.pyplot as plt
import numpy as np


def star():

    t = np.arange(0, 4*np.pi, 0.01)
    x = 12 * np.cos(t) + 8*np.cos(1.5*t)
    y = 12 * np.sin(t) + 8*np.sin(1.5*t)

    plt.plot(x, y)
    plt.savefig('star.png')


star()


def rotate_star(alpha, x_0 = 0, y_0 = 0, x_1 = 20, y_1 = 0):

    t = np.arange(0, 4*np.pi, 0.01)
    x = 12 * np.cos(t) + 8*np.cos(1.5*t)
    y = 12 * np.sin(t) + 8*np.sin(1.5*t)

    X = x_0 + (x - x_1)*np.cos(alpha) - (y - y_1)*np.sin(alpha)
    Y = y_0 + (y - y_1)*np.cos(alpha) + (x - x_1)*np.sin(alpha)

    plt.plot(X, Y)
    plt.savefig('rotate_star.png')


rotate_star(np.pi)