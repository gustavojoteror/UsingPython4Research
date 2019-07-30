# GOAL: investigate the correlation between different attributes of the data.

# There are many different kinds of correlations, and by default, the function uses what is called Pearson correlation
# whices estimates linear correlations in the data.
# Two attrivutes of the data: x and y. The pearson correlation coefficient between x and y approaches +1 as the points
# in xy scatterplot approach a stright upward line.
# What this means: a large positive correaltion coefficient indicates that the two flavor attrivutes in question tend
# to either increase or decrease together.


import numpy as no
import pandas as pd
import matplotlib.pyplot as plt

whisky= pd.read_csv('whiskies.txt')
whisky['Region']= pd.read_csv('regions.txt')
flavors = whisky.iloc[:, 2:14]

corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)

# let's vosia;ize the correlation
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig('corr_flavors.pdf')

corr_whisky = pd.DataFrame.corr(flavors.transpose())    # making rows into columns and columns into rows to study the distillery
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis('tight')
plt.colorbar()
plt.savefig('corr_whisky.pdf')
