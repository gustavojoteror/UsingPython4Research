# indexing numpay arrays: first index specifies the row and the second index the column.
# index starts from 0 and stops before hitting th stop index
import numpy as np

x =  np.array([1,2,3])
y =  np.array([2,4,6])
X =  np.array([[1,2,3], [4,5,6]])
Y =  np.array([[2,4,6], [8,10,12]])

# vectors
print(x[2])
# print(x[4]) # IndexError: index 4 is out of bounds for axis 0 with size 3
print(x[0:2]) # it stops before x[2]; therefore the output is 1,2 without including 3
z = x + y   # element wise summation
print(z[:])   #gives me the whole row
print('=====')
# matrices
print(X[:,1])   # gives back all the elements of the second column of X
print(Y[1,:])   # gives back all the elements of the second row (last) of Y

zz = X[:,1] + Y[:,1]        # gives back a one-dimensional array (a vector) with two elements
print(zz)
zzz = X[1,:] + Y[1,:]       # gives back a one-dimensional array (a vector) with three elements
print(zzz)

# this next two lines are exactly the same
print(X[1,:])
print(X[1])

# what would happen if we sum two lists?
print([2,4]+[6,8])    # this doesn't make an element wise summation, instead it cocatenates the lists!!
print(np.array([2,4])+np.array([6,8]))    # but if we turn the lists into np.array then an element wise summation happens.
