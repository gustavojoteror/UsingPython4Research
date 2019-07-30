import numpy as np

# uniformly spaced arrays (linearly and logarithmic)
# linearly spaced array
lin_x = np.linspace(0, 100, 10)   #(starting value, ending value, size of the array)
print(lin_x)

# logarithmic spaced array
log_x = np.logspace(1, 2, 10)   #(starting log_10(value), ending log_10(value), size of the array)
            # log_10(10)= 1, log_10(100)=2
print(log_x)

log_x2 = np.logspace(np.log10(250), np.log10(500), 10)
print(log_x2)

# shapes of arrays
X = np.array([[1, 2, 3], [4, 5, 6]])
print(X.shape)      # gives back: a tuple with (# of rows, # of columns
print(X.size)       # gives back: # of elements
# shape and size do not have () because they are data attributes (not a method)

x = np.random.random(10)       # will produce 10 randome number in the interal 0 to 1
print(x)
print(np.any(x>0.9))            #  at least one element is greater than 0.9
print(np.all(x>=0.1))           #  are all elements is greater than 0.1