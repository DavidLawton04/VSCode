#pythonproj1

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

iterations = range(1,300)

def func(a,x):
    for i in iterations:
        x = a * x * (1 - x)
    return x

xlist = np.arange(0,1,0.1)
alist = np.arange(0,4, 0.0001)
glist=[]

plt.figure('bifurc')
for x0 in xlist:
    for g in alist:
        glist.append(func(g,x0))
    plt.plot(alist, glist, '.k', markersize=0.07)
    glist=[]
'''plt.savefig('/home/dj-lawton/VSCode/bifurc.pdf')'''
plt.show()