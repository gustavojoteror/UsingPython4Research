# GOAL find which is the nearest neighbor
import matplotlib.pyplot as plt
import numpy as np
from functions import *

# loop over all point
    # compute the distance between the point p and every other point
# sort distane and return those k points that are nearest to point p.

def find_nearest_neighbors(p, points, k=5):
    """
    Find the k-nearest neighbots of point p in the array of points and return their indices.
    :param p:       point in question
    :param points:  array of points
    :param k:       number of neighbors we want
    :return:
    """
    dist = np.zeros(points.shape[0])
    for i in range(len(dist)):
        dist[i] = distance(p, points[i])
    ind = np.argsort(dist)
    return ind[0:k]


k = 2
points  = np.array([[1,1], [1,2], [1,3], [2,1], [2,2],[2,3], [3,1], [3,2], [3,3]])
p       = np.array([2.5, 2.2])


ind = find_nearest_neighbors(p, points, k)
p_neighbors = points[ind]

plt.plot(points[:,0], points[:,1], 'ro', label='array of points')        # array of points
plt.plot(p[0], p[1], 'bo', label='point')
plt.plot(p_neighbors[:,0], p_neighbors[:,1], 'ko', markersize=12, fillstyle='none', label='nearest neighbors')
plt.axis([0.5, 4.5, 0.5, 4.5])
plt.legend()
plt.show()
# fillstyles: https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/marker_fillstyle_reference.html


# building our functions
# distances = np.zeros(points.shape[0])
# for i in range(len(distances)):
#     distances[i] = distance(p, points[i])
#     # what we want now is an index vector that would sort the array: np.argsort
#
# ind = np.argsort(distances)     # this function returns an array of indeces. An index of 0 is the smaller value
# print(ind)
# print(distances[ind])
