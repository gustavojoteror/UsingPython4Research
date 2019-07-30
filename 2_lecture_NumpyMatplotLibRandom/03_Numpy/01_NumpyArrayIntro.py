# NumPy is a Python module designed for scientific computation (numpy.org)
# Usefule feature of NumPy
# 1. NumPy arrays are n-dimensioanl array
# 2. NumPy provides tools for integrating your code with exisiting C, C++, and Fortran code
# 3. NumPy provides tools to help you perform linear algebra, generate random numbers.

# NumPy arrays: data type from numpy to represent vectors and matrices.
#               fixed size when they are constructed

# to import numpy
import numpy as np

zero_vector = np.zeros(5)      # creates a vector of dimension 5 with all elements which are equal to 0.
zero_matrix = np.zeros((5, 3))   # creates a matrix with 5 rows and 3 columns
# the only difference in the definition of a vector and a matrix is the argument given. I one case is a integer and
# in the other one is a tuple with two integers.
print(zero_vector)
print(zero_matrix)

# you can even create higher dimension matrices
zero_highermatrix = np.zeros((5, 3,4))
print(zero_highermatrix)

one_vector = np.ones(5)     # same as above but now all the elements are 1s
print(one_vector)
empty_vector = np.empty(5)  # a vector of 5th order but it is not initialized. Howerver, the memory is allocated in the computer
print(empty_vector)

# vectors (or one dimensional arrays) are defined in lower cases
# matrices are defined in upper cases.
# vectors:
x = np.array([1,2,3])
y = np.array([2,4,6])
# matrices:
M = np.array([[1,3], [5,9]])  # ( [first row], [second row], .... , [n-row])
print('=============')
print(M)
M.transpose()
print(M)                # the matrix is not transpose becasue  the method doesn't modify the object!
print(M.transpose())

# To access the data A[row,column], remember that python array start from zero.