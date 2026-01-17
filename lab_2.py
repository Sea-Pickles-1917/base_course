import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def circle(a, time):
    alpha = np.arange(0, 2*np.pi, 0.1)
    R = a * time
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')


def animate(i):
    ball.set_data(circle(a=0.005, time=i))
    return ball


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=20)
ani.save('animation_4.gif', writer="pillow")