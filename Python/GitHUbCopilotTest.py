import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button

# Create an evenly spaced set of points between 0 and 2*pi
points = np.linspace(0, 2*np.pi, 20)
x, y = np.meshgrid(points, points)

# Define your constant k
k = 100 # replace with your actual value


# Your iterative function
def mapfunc(x, y):
    p = np.sin(x)
    x = x + y + (k * p)
    y = y + (k * p)
    return x, y


# Prepare the figure and the button
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
colours = y.ravel()
scat = ax.scatter(x, y, s=2, c=colours, cmap='nipy_spectral')


# Initialization function
def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(0, 2*np.pi)
    scat.set_offsets(np.c_[x.ravel(), y.ravel()])  # set the initial state of the scatter plot
    return scat,

# Animation function
def animate(i):
    global x, y
    if i == 0:
        return scat,
    x, y = mapfunc(x, y)
    x = np.mod(x, 2*np.pi)  # wrap x to the interval [0, 2π]
    y = np.mod(y, 2*np.pi)  # wrap y to the interval [0, 2π]
    scat.set_offsets(np.c_[x.ravel(), y.ravel()])
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=35, interval=100, blit=True)


# Start the animation paused
ani.save('ChaosAssignmentGIFk10^-3.gif',  
          writer = 'ffmpeg', fps = 10) 