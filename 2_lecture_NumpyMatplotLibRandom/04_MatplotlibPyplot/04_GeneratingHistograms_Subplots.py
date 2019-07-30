import matplotlib.pyplot as plt
import numpy as np


# histogram: frequency distribution
# A histogram is an accurate representation of the distribution of numerical data. It is an estimate of the probability distribution o

#normal distributions
plt.figure()
x=np.random.normal(size=1000)
plt.hist(x)

# to normalize the histogram
plt.figure()
plt.hist(x, normed=True, bins=np.linspace(-5,5,21))
plt.axis([-5,5,0,0.4])



# To construct a histogram, the first step is to "bin" (or "bucket") the range of values—that is, divide the entire range
# of values into a series of intervals—and then count how many values fall into each interval.
# The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent,
# and are often (but are not required to be) of equal size

# for an bin or intervale: 2 points is 1 bin, 3 points are 2 bins, etc...

# plt.subplots()      # (# of rows, # of columns, plot number) # the incremenet goes through rows first
#           plt.subplots(2,3,i)
#           ________________________
#           |   1   |   2   |   3   |
#           |_______|_______|_______|
#           |   4   |   5   |   6   |
#           |_______|_______|_______|

#   gamma distributions
x=np.random.gamma(2, 3, size=1000)
plt.figure()
plt.subplot(221)            # same as plt.subplot(2, 2, 1)
plt.hist(x,bins=30)
#normalized
plt.subplot(222)            # same as plt.subplot(2, 2, 2)
plt.hist(x,bins=30, normed=True)
# cumulative
plt.subplot(223)            # same as plt.subplot(2, 2, 3)
plt.hist(x,bins=30, cumulative=True)
# all
plt.subplot(224)            # same as plt.subplot(2, 2, 4)
plt.hist(x,bins=30, normed=True, cumulative=True, histtype='step')

plt.show()



