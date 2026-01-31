import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

t = np.arange(0.01 , 4 * np.pi, 0.01)
R = 1

x = R * np.cos(t)
y = R * np.sin(t)
z = R * t

ax.plot(x, y, z, label='Dich')

plt.savefig('curve.png')