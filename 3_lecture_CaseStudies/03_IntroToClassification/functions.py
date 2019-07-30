import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

def distance(p1, p2):
    """
    Finds the distance between p1 and p2
    :param p1:
    :param p2:
    :return distance:
    """
    return np.sqrt(np.sum(np.power(p2-p1, 2)))


def majority_vote(votes):
    """
    Returns the most common element in votes
    Count the number of votes each word occurs in text (str). Return dictionary where keys are unique words
    and values are word counts. We make the input text into lower cases and the punctuations are skipped.
    This function calcualtes what is called in statistics as mode.
    :param vote:
    :return:
    """

    vote_counts = {}        # dictionary
    for vote in votes:
        # known word
        if vote in vote_counts:
            vote_counts[vote] += 1
        # unknown word
        else:
            vote_counts[vote] = 1

    # print(vote_counts)
    # but who is the winner?
    winners = []
    max_votes = max(vote_counts.values())

    # for (,) this is a tuple
    for vote, count in vote_counts.items():
        if count == max_votes:
            winners.append(vote)

    # what is we have multiply winners? Well we select one randomly

    return random.choice(winners)


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

def knn_predict(p, points, outcomes, k=5):
    """
    :param p:           point we want to classify
    :param points:      array of points
    :param outcomes:    classification of given points
    :param k:           number of neighbors used
    :return: classification prediction
    """

    #find k nearest neightbors
    ind = find_nearest_neighbors(p, points, k)
    # predict the class of p based on majority vote
    return majority_vote(outcomes[ind])

def generate_synth_data(n_obs=50, n_class=2):
    """
    Create two sets of points from bivariate normal distribution
    :param n_obs:
    :param n_class:
    :return:
    """
    data     = np.concatenate((ss.norm(0,1).rvs((n_obs,n_class)), ss.norm(1,1).rvs((n_obs,n_class))), axis=0)
    outcomes = np.concatenate((np.repeat(0,n_obs), np.repeat(1,n_obs))) # this is the same as np.concatenate(np.zeros(n_obs), np.ones(n))
    return (data, outcomes)

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
    xx, yy = np.meshgrid(xs,ys)

    prediction_grid = np.zeros(xx.shape, dtype = int)  # we say they are integer because the class types are either 0 or 1
    for i,x in enumerate(xs):   #enumarate construct)
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)


    return (xx, yy, prediction_grid)

def plot_prediction_grid (xx, yy, prediction_grid, predictors, outcomes, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)