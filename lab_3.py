import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def butterfly(e=2.718):
    time = np.arange(0, 12*np.pi, 0.1)
    x = np.sin(time)*(e**np.cos(time) - 2*np.cos(4*time) + np.sin(time/12)**5)
    y = np.cos(time)*(e**np.cos(time) - 2*np.cos(4*time)+ np.sin(time/12)**5)
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')


def animate(i):
    ball.set_data(butterfly())
    return ball


edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=20)
ani.save('animation_6.gif', writer="pillow")