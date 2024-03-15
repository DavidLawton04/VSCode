import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

#Mapping function
def mapfunc(x, y, k):
    p = np.sin(x)
    x = x + y + (k * p)
    y = y + (k * p)
    return x, y


#Evenly spaced set of points between 0 and 2*pi
points = np.linspace(0, 2*np.pi, 14)
x, y = np.meshgrid(points, points)
colour = y.ravel()


#Plotting function
def plotter(k):
    global x,y
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(0, 2*np.pi)
    plt.title(f'Motion of System for k = {k}')
    for i in range(100):
        x, y = mapfunc(x, y, k)
        x = np.mod(x, 2*np.pi)
        y = np.mod(y, 2*np.pi)
        scat = ax.scatter(x, y, s=0.5, c=colour, cmap='nipy_spectral')
        scat.set_offsets(np.c_[x.ravel(), y.ravel()])
    plt.savefig(f'Python/Chaos/ChaosAssignmentstillk{k}.pdf')


#Create plot for list of k values
for k in [10**-3, 0.1, 0.5, 0.971635, 1, 1.5, 2]:
    plotter(k)
    print(f'k = {k} done')