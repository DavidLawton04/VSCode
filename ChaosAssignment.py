import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# mapping function
def mapfunc(x, y, k):
    p = np.sin(x)
    x = x + y + (k * p)
    y = y + (k * p)
    return x, y


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
    x, y = mapfunc(x, y, k)
    x = np.mod(x, 2*np.pi)  # wrap x to the interval [0, 2π]
    y = np.mod(y, 2*np.pi)  # wrap y to the interval [0, 2π]
    scat.set_offsets(np.c_[x.ravel(), y.ravel()])
    return scat,


# evenly spaced set of points between 0 and 2*pi
points = np.linspace(0, 2*np.pi, 150)
x, y = np.meshgrid(points, points)
colours = y.ravel()



def create_animation(k):
# figure
    global ax, scat
    fig = plt.figure()
    ax = fig.add_subplot(111)
    scat = ax.scatter(x, y, s=0.5, c=colours, cmap='nipy_spectral')
# Create animation
    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=10, blit=True)

    ani.save(f'ChaosAssignmentGIFk{k}.gif',  
          writer = 'ffmpeg', fps = 8) 
    
for k in [10**-3, 0.1, 0.5, 1, 1.5, 2]:
    create_animation(k)
    print(f'k = {k} done')