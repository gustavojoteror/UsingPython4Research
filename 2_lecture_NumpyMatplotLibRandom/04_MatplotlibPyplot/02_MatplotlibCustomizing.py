# customize
# legend()
# axis()
# xlabel()
# ylabel()
# savefig()

import matplotlib.pyplot as plt
import numpy as np

# for latex!!!
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
################################

xmin= -0.5
xmax= 10.5
ymin= -5
ymax= 105

x = np.linspace(0, 10, 20)
y1 = x**2.0
y2 = x**1.5

plt.plot(x, y1, "bo-", linewidth=2, markersize=4, label='y1')         # label="" for the legend
plt.plot(x, y2, "gs-.", linewidth=2, markersize=4, label='y2')
#customizing
plt.xlabel(r"$\displaystyle X\approx \frac{\alpha}{\beta}$")  # plt. has latex available
plt.ylabel("$Y$, Y")
plt.axis([xmin,xmax,ymin,ymax])
plt.legend(loc='upper left')   #loc for location
plt.savefig('myPlot.pdf')
plt.show()


# How i made the latex symbols to work

# import numpy as np
# import matplotlib.pyplot as plt
#
#
# # Example data
# t = np.arange(0.0, 1.0 + 0.01, 0.01)
# s = np.cos(4 * np.pi * t) + 2
#
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')
# plt.plot(t, s)
#
# plt.xlabel(r'\textbf{time} (s)')
# plt.ylabel(r'\textit{voltage} (mV)',fontsize=16)
# plt.title(r"\TeX\ is Number "
#           r"$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
#           fontsize=16, color='gray')
# # Make room for the ridiculously large title.
# plt.subplots_adjust(top=0.8)
#
# plt.savefig('tex_demo')
# plt.show()