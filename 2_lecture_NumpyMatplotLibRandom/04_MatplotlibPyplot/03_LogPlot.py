import matplotlib.pyplot as plt
import numpy as np

# making on or both axis logarithmic.
#       semilogx(): function to plot x-axis in log scale but y-axis in original scale
#       semilogy(): function to plot y-axis in log scale but x-axis in original scale
#       loglog(): function to plot bots axis in log scale

# below is the same as in 02_MatplotlibCustomizing
# the only difference is that we dont use the function plot, instead we use loglog()
# also we can use a uniform spacing in x in log scale
# for latex!!!
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
################################

xmin= -0.5
xmax= 10.5
ymin= -5
ymax= 105

x = np.logspace(-1, 1, 40)      #log(0.1)=-1, log(1)=10
y1 = x**2.0
y2 = x**1.5

plt.loglog(x, y1, "bo-", linewidth=2, markersize=4, label='y1')         # label="" for the legend
plt.loglog(x, y2, "gs-.", linewidth=2, markersize=4, label='y2')
#customizing
plt.xlabel(r"$\displaystyle X\approx \frac{\alpha}{\beta}$")  # plt. has latex available
plt.ylabel("$Y$, Y")
plt.axis([xmin,xmax,ymin,ymax])
plt.legend(loc='upper left')   #loc for location
plt.savefig('myPlot.pdf')
plt.show()