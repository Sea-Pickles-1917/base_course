import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0,2 * np.pi, 100)

n = 3
l = 1
m = 2

x = np.outer(phi, np.cos(theta)) + l * theta
y = np.outer(phi, np.sin(theta)) + m * theta
z = n * theta

ax.plot(x, y, z, label='Dich')

plt.savefig('conoid.png')