import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def star(alpha):
    t = np.arange(0, 2*np.pi, 0.1)
    x = 12*np.cos(t) + 8*np.cos(1.5*t)
    y = 12*np.sin(t) + 8*np.sin(1.5*t)

    X = (x*np.cos(alpha) - y*np.sin(alpha))
    Y = (y*np.cos(alpha) + x*np.cos(alpha))
    return X, Y

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')


def animate(alpha):
    ball.set_data(star(alpha))
    return ball


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=20)
ani.save('animation_4.gif', writer="pillow")