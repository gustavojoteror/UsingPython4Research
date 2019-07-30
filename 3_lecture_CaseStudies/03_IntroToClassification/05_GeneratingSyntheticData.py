#GOAL generate two end data points where the first end point are from class 0 and the secodn end poitns are from class 1.
# This data are known as synthetic data.
import matplotlib.pyplot as plt
import scipy.stats as ss
import numpy as np

# A normal continuous random variable. The location (loc) keyword specifies the mean. The scale (scale) keyword
# specifies the standard deviation. As an instance of the rv_continuous class, norm object inherits from it a
# collection of generic methods (see below for the full list), and completes them with details specific for this
# particular distribution. rvs(loc=0, scale=1, size=1, random_state=None): random variates
#ss.norm(0,1).rvs((5,2))  rvs(rows, columns)

def generate_synth_data(n=50, n_class=2):
    """
    Create two sets of points from bivariate normal distribution
    :param n_obs:
    :param n_class:
    :return:
    """
    data     = np.concatenate((ss.norm(0,1).rvs((n_obs,n_class)), ss.norm(1,1).rvs((n_obs,n_class))), axis=0)
    outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n))) # this is the same as np.concatenate(np.zeros(n_obs), np.ones(n))
    return (data, outcomes)


# n_obs = 5   #number of observations
# n_class=2   #number of classes

n = 20
(data, outcomes) = generate_synth_data(n)
plt.figure()
plt.plot(data[:n,0], data[:n,1], 'ro')      # the first n points are for the first class
plt.plot(data[n:,0], data[n:,1], 'bo')      # an the last n points are for the second class
plt.show()
plt.savefig('bivardata.pdf')