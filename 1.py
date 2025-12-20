import matplotlib.pyplot as plt
import numpy as np

def hyperbola(x_min, x_max, N):
    x = np.linspace(x_min,x_max, N)
    y = 1 / (x + 0.1)

    plt.plot(x, y)
    plt.savefig('fig_3.png')

hyperbola(-5, 5, 100)
plt.close()

def log_spiral(b):
    phi = np.arange(0, 8*np.pi, 0.01)
    r = np.exp(b * phi)

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)
    plt.savefig('log.png')

log_spiral(0.3)
plt.close()