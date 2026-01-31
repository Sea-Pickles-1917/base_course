import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)

a = 2
b = 1
c = 3

x = a *np.outer(np.cos(phi), np.sinh(theta))
y = b * np.outer(np.sin(phi), np.sinh(theta))
z = c * np.sinh(theta)

ax.plot(x, y, z, label='Dich')

plt.savefig('hiperbol.png')