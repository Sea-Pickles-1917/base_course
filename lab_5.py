import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

x = [0.1]
y = [0.1]
C = 0.3
D = 0.33


def animate(i):
    x.append(x[i-1]**2 - y[i-1]**2 + C)
    y.append(2 * x[i-1] * y[i-1] + D)

    fractal.set_data(x, y)
    return fractal


fig, ax = plt.subplots()
fractal, = plt.plot([], [], 'o', color='r')


plt.axis('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

ani = FuncAnimation(fig, animate, frames=100, interval=20)
ani.save('animation_5.gif', writer="pillow")