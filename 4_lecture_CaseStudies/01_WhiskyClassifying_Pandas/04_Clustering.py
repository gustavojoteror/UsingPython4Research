# GOAL: to cluster whiskeys based on their flavor profiles using a clustering method from scikit-learn
# The method we will use is: Spectral Co-Clustering
#                               consider a list of words and a list of documents. A document can have several words.
#                               the goal of the method is to find clusters that consists of sets of words and sets of
#                               documents that ofter go together.
#                               The term co-clusters: refers to the idea of simultaneously find both clusters of words
#                               and clusters of documents.
#                               Spectral refers to the use of eigenvalues and eigenvectors of some matrix.
#                               The list of words and document can be a matrix
from sklearn.cluster.bicluster import SpectralCoclustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

whisky= pd.read_csv('whiskies.txt')
whisky['Region']= pd.read_csv('regions.txt')
flavors = whisky.iloc[:, 2:14]


corr_flavors = pd.DataFrame.corr(flavors)
corr_whisky = pd.DataFrame.corr(flavors.transpose())    # making rows into columns and columns into rows to study the distillery

model = SpectralCoclustering(n_clusters=6, random_state=0)      #n_clusters: number of clusters you want the method to come up with
model.fit(corr_whisky)
print(model.rows_)        # number of row clusters x number of rows in the data matrix
# it retunrs true or false
print(np.sum(model.rows_, axis=1))     #axis=0 rows, axis=1 columns Printing the number of observation per cluster
print(np.sum(model.rows_, axis=0))     #Printing the number of cluster per observation: should be all 1s
print(model.row_labels_)     #Tells to which cluster each observation is part of (goes from 0 to 5, 6 clusters)

whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)
print(whisky.head())
#     Selecting data by row numbers (.iloc)
#     Selecting data by label or by a conditional statment (.loc)
#     Selecting in a hybrid approach (.ix) (now Deprecated in Pandas 0.20.1)
whisky = whisky.ix[np.argsort(model.row_labels_)]
# numpy.argsort() Returns the indices that would sort an array. Perform an indirect sort along the given axis using the algorithm
# specified by the kind keyword. It returns an array of indices of the same shape as a that index data along the given axis in sorted order.
whisky = whisky.reset_index(drop=True)      # reschuffling the rows and columns of the table
whisky.to_csv(r'whiskyRearranged.txt', header=True, index=True, sep=' ', mode='a')
correlation= pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlation)

plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title('Original')
plt.axis('tight')
plt.subplot(122)
plt.pcolor(correlations)
plt.title('Rearranged')
plt.axis('tight')
plt.savefig('correlations.pdf')