import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

T = 18
h = 0.5
L = 20 - h
a = 1
CFL = 0.6
tau = h * CFL / a
N = int(L/h)
x = np.linspace(0, L, N+1)
y = np.zeros((int(T/tau), N + 1))
y0 = np.sin(4 * np.pi * x / (L + h))

y00 = np.zeros(N+1)
y00[14:26] = 1

y[0] = y00
y_next = y00



for i in range(int(T/tau) - 1):
    for j in range(N-1):
        y_next[j+1] = (-1)*y[i][j+1] * (CFL**2 - 1) - (CFL/2 - CFL**2/2)*y[i][j+2] + y[i][j] * (CFL/2 + CFL**2/2)
    y_next[0] = (-1)*y[i][0] * (CFL**2 - 1) - (CFL/2 - CFL**2/2)*y[i][1] + y[i][-1] * (CFL/2 + CFL**2/2)
    y_next[-1] = (-1)*y[i][-1] * (CFL**2 - 1) - (CFL/2 - CFL**2/2)*y[i][0] + y[i][-2] * (CFL/2 + CFL**2/2)
    y[i+1] = y_next


fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)



def init():
    line.set_data([], [])
    return line,


def animate(i):
    global y
    x = np.linspace(0, L, N + 1)
    y_anim = y[i]
    line.set_data(x, y_anim)
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=int(T/tau), interval=30, blit=True)

anim.save('sine_wave.gif', writer='imagemagick')

plt.show()

