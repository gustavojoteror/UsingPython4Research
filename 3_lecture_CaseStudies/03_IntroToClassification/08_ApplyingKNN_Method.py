# GOAL apply the knn method

# SciKitlearn is an open source machine learning library for python.
#       It has a knn classifier.

# We will apply our homemade knn method and the scikitlearn methods to a data from:Ron Risher in 1933
# Data: 150 Iris flowers.
#               50 from each of the three different species.
#               For each flow we have: Sepal length, sepal width, petal length and petal width
import matplotlib.pyplot as plt
from sklearn import datasets
from functions import *
import numpy as np
iris = datasets.load_iris()

print(iris['data'])

# for simplicity we will just look at the first two covariates or predictors in this example
predictors = iris.data[:, 0:2]      # remember the x index 2 will not be included
outcomes = iris.target

plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], 'ro')
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], 'go')
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], 'bo')
# plt.show()
plt.savefig('iris.pdf')

##############
# let use our code
k=10
filename = 'iris_grid.pdf'
limits = (4, 8, 1.5, 4.5)
h= 0.1

xx, yy, prediction_grid = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, predictors, outcomes, filename)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)

my_predictions = np.array([knn_predict(p, predictors, outcomes, k) for p in predictors])

print(sk_predictions==my_predictions)
print(np.mean(sk_predictions==outcomes)*100)
print(np.mean(my_predictions==outcomes)*100)