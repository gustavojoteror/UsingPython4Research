# GOAL find which is the nearest neighbor
import matplotlib.pyplot as plt
import numpy as np
from functions import *

def knn_predict(p, points, outcomes, k=5):
    #find k nearest neightbors
    ind = find_nearest_neighbors(p, points, k)
    # predict the class of p based on majority vote
    return majority_vote(outcomes[ind])


k = 4
points  = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
p       = np.array([2.5, 2.7])
outcomes= np.array(['evil', 'evil', 'evil', 'evil', 'evil', 'good', 'good', 'evil', 'good']) # two classification classes, either 0 or 1

print((len(outcomes) == points.shape[0]))

print(knn_predict(p, points, outcomes, k))

ind = find_nearest_neighbors(p, points, k)
p_neighbors = points[ind]

plt.plot(points[:,0], points[:,1], 'ro', label='array of points')        # array of points
plt.plot(p[0], p[1], 'bo', label='point')
plt.plot(p_neighbors[:,0], p_neighbors[:,1], 'ko', markersize=12, fillstyle='none', label='nearest neighbors')
plt.axis([0.5, 4.5, 0.5, 4.5])
plt.legend()
plt.show()