# Matplotlib is a python plotting library that produces high quality figures.
# Pyplot is a collection of function (not all matplotlib) that makes matplotlib work as matlab.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,np.pi*2,20)
y = x**2.0

fig1 = plt.plot(np.sin(x))   # this will print the array with respect to its location in the array
plt.show()
plt.pause(5)
plt.close()
# keyword argument: is an argument which is supplied to the function by explicitly naming each parameter and specifying its value
y2 = x**1.5
fig2 = plt.plot(x, y, "bo-", linewidth=2, markersize=4)         # the first argument is the x coordiante and the second one y coordinate
fig3 = plt.plot(x, y2, "gs-.", linewidth=2, markersize=4)         # the first argument is the x coordiante and the second one y coordinate
plt.show()
