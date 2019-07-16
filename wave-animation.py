%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(5, 3))
ax.set(xlim=(-10, 10), ylim=(-1.2, 1.2))

x = np.linspace(-10, 10, 100)
t1 = np.linspace(1, 6, 100)
t2 = np.linspace(6, 1, 100)
t = np.append(t1, t2)

X2, T2 = np.meshgrid(x, t)
kt = np.pi/20 * T2

F = np.sin(X2 * kt)

line = ax.plot(x, F[0, :], color='k', lw=2)[0]

def animate(i):
    line.set_ydata(F[i, :])
    if i < 10:
        ax.set_title('Frame #00' + str(i))
    elif i < 100:
        ax.set_title('Frame #0' + str(i))
    else:
        ax.set_title('Frame #' + str(i))

anim = FuncAnimation(
    fig, animate, interval=25, frames=len(kt)-1)

fig.show()
anim.save('line.gif', writer='imagemagick')
