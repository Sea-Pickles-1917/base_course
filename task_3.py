import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0,2 * np.pi, 100)

h = 2

x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = h * theta

ax.plot(x, y, z, label='Dich')

plt.savefig('helicoid.png')