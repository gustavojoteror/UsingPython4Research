import numpy as np

# numpy arrays can be indexed with other arrays or other seequence-like objects like lists

z1 = np.array([1,3,5,7,9])
z2 = z1 +1                  # will add 1 to all the elements of the array z1

print(z1)
print(z2)

ind = [0,2,3]
print(z1[ind])      # this gives me access to the elements located in the index specified in ind

ind_np = np.array([0,2,3])
print(z2[ind_np])

print(z1 > 6)       # does an element wise comparison and gives back a boolean array (or logical array)
print(z1[z1 > 6])   # it return the elements which are true for the comparison
# we are using the logical array as index vector to access the elements of the array. We can use this logical array
# for other vectors as shown below
z3 = z1[z1 > 6] + z2[z1 > 6]
print(z3)

# we can also construct the logical vector
ind_log = z1 > 6

z4 = z1[ind_log] + z2[ind_log]
print(z4 == z3)

# word of caution: when modifying a slice of a vector the original array will be also modified. In contract when you index
# an array, in which a copy of the original data is return

# let's try first with slicing
w = z1[0:3]
print(w)
w[0] = 3        # by doing this we are also modifying z1
print(z1)
# now indexing
index= [0,1,2]
v = z2[index]
print(v)
v[0] =0         # instead by using indexing z2 is not modified
print(v)
print(z2)

