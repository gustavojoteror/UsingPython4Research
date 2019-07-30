import numpy as np
import math

x = np.array([1,3, 5])
y = np.array([1,5, 9])

print(x.mean())             # mean() it is a function
print(y.mean())

print(x.shape)              # shape it is a data atribute
print(y.shape)

print(math.pi)
print(math.sqrt(10))

print(math.sin(math.pi/2))

from math import pi         # to import only pi from the library math

# namespaces
print(math.sqrt(2))
print(np.sqrt(2))           # the function of np has more features
print(np.sqrt([2,3,4]))     # the function of np has more features

name = "gus"
print(type(name))           # to know the type of object
print(dir(name))            # this will give me all the method available to this object type
print(str)            # this will give me all the method available to this object type

# help(name.upper())      # this is wrong we are asking for help on "GUS" not the method
# help(name.upper)        # this will give you help on the method


###############################
# numbers are a python object that provides
# three numerical types: integer, float and complex
print(127+150)
print(127*33)
print(127**10)
print(127**100)   # python has unlimited precision for integers
print(15./7)       # floating point division
print(15/7)       # floating point division
print(15//7)      # integer division (lower)
print(15.//7)      # integer division (lower)