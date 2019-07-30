# GOAL: plot the prediction grid. Ask our classifier to predict the class all the points to a rectangular region.
import matplotlib.pyplot as plt
import numpy as np
from functions import *

def make_prediction_grid(predictors, outcomes, limits, h, k):
    """
    Classify each point on the prediction grid.
    :param predictors:
    :param outcomes:
    :param limits:
    :param h:
    :param k:
    :return:
    """
    (x_min, x_max, y_min, y_max) = limits   # limits should consists of a tuple with 4 elements that
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs,ys)      # generate 2, two dimensional arrays: one containing the x values and the other one the y values
    # xs and ys are 1 dimensional arrays. xx and yy are 2-dimensional

    prediction_grid = np.zeros(xx.shape, dtype = int)  # we say they are integer because the class types are either 0 or 1
    for i,x in enumerate(xs):   #enumarate construct)
        for j,y in enumerate(ys):
            # enumarate is useful when dealing with sequences and when we would like to have access simultaneously to two
            # things: elements and index values.
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
            # [j,i] because j corresponds to y values, and when we specify an index using square brackets, the first
            # value, the first argument, corresponds to the row of the array
            # i is x and are the columns of the array


    return (xx, yy, prediction_grid)


#Enumerate object
seasons = ['spring', 'summer', 'fall', 'winter']
Enum = enumerate(seasons)  # this is an enumerate object: each element is a tuple consisting of (index, value)
print(list(Enum))

for ind, season in enumerate(seasons):   # we are loopingover the enumerate object.
    print(ind, season)
