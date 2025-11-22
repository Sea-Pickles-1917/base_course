from lec_my_module import gravity_const as g
import numpy as np

x_0 = 0
y_0 = 0

v_x = 7
v_y = 4

step = 0.1

t = np.arange(0, 5, step)
coords = []
for t in np.arange(0, 5, step):

    x = x_0 + v_x*t
    y = y_0 + v_y*t - g * t ** 2 / 2

    coords.append([t, x, y])
coords = np.zeros((len(t), 3))
coords[:, 0] = t
coords[:, 1] = x
coords[:, 2] = y
print(coords)
