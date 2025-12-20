import matplotlib.pyplot as plt
import numpy as np


def stairway(N):
    x = np.arange(0, N, 0.001)
    y = x // 1

    plt.plot(x, y)
    plt.savefig('stairway.png')
    plt.close()

stairway(5)