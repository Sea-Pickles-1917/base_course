import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

theta = np.linspace(0,2 * np.pi, 100)
R = 2

x = R * np.cos(theta) ** 3
y = R * np.sin(theta) ** 3
z = np.cos(2 * theta)

ax.plot(x, y, z, label='Dich')

plt.savefig('curve1.png')