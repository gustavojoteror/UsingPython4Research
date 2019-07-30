import numpy as np
import pandas as pd

#Pandas is a python library that provides data structures and functions for working with structured data, primarily
# tabular data. Pandas is built unto of numpy.
# Pandas datas structures: Series (1D array like) and DataFrames (2D array like). Both objects contain additional
# information about the data called metadata

################################################################################
# Panda series

# simple contruction
x= pd.Series([6, 3 , 8, 6])  #input is a list of arguments
print(x)        # Data rray is shown in the right column and the index in the left column which is an array data labels
# we didn't define any index explicitly so Pandas took the default: sequence of integers starting at 0 increasin one by one

x= pd.Series([6, 3 , 8, 6], index=['q','w','e','r'])  #specifying the index explicitly
print(x)
print(x["w"])       #take just the value from index w
print(x[["w", "r"]])  # we give a list of index

# contruction with a python dictionary
age = {"Tim": 29,   "Gus": 31, "Daniela": 29, "Ximena": 6, "Fini": 69}
x = pd.Series(age)
print(x)            # the index of the series are the keys of the dictionary in sorted order and the values are the
                    # value objects in the dictionary

################################################################################
# Panda data frames: represent table like data; they have both row and column index

# contructing with a dictionary where the value objects are lists or numpy arrays of equal lengths
data = {"name": ['Tim', 'Gus', 'Xime', 'Fini'],
       "age": [29, 31, 6, 69],
       "address": ['USA','NL', 'PN', 'VZ']}
# the keys are: name, age and address, and the values are the lists of either strings of numbers
x = pd.DataFrame(data, columns=['name', 'age', 'address'])     # first argument is the data (the dictionary we created) and the
        # second argument are the columns that we would like to include as well as the order in which they should appear
print(x)    #again we didn't specify the index so it goes from 0 to 3
x = pd.DataFrame(data, columns=['name', 'age', 'address'], index=['e', 'b', 'x', 'a'])
print(x)

# retriving data:
# 1: By using dictionary like-notation
print(x['name'])
# 2. We can specify the name of the column as an attritube
print(x.age)
print(x.index)

# re indexing the data
ind= sorted(x.index)    # alphabetical index
print(x.reindex(ind))

################################################################################
# PArithmetic operations: Series and dataframes
#       add two series objects together: the data allignment happens by index: entries in the series that have the same
#       index are added together in the same way as you add twp numpy arrays
#       IF THE INDICES DO NOT MATCH: NAN will be the result

x= pd.Series([6, 3 , 8, 6], index=['q','s','e','r'])
y= pd.Series([7, 3 , 5, 2], index=['q','t','e','s'])
print(x)
print(y)
print(x+y)


