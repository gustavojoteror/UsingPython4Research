import copy
# static typed languages; C, C++
        #type checking in performed during compiling time
# dynamic typed: python
        #type checking is performed at run time

# always: variable, object and reference.
x= 3
# python created an object first (3)
# then it gives a name to that object (x)
# and then it insert a reference from the name of the variable to the actual object (x -> 3)
# Variales names always link to objects, never to oterh variables.
# Therefore the variable is a reference to the given object.
# Important to keep in mind the distinction between: mutable and inmutable objects.
#           mutable objects: list, set and dictionaries. Mutable objects can be identical in content and yet be actually different objetcs
#         inmutable objects: tuples, numbers and strings   (cannot be altered after they've been created)

y = x       # here y is refering to the object 3 (not to the variable x)
y = y -1    # this creates a new object (3-1=2) and removes the previos reference of y ->3 and insert a new y->2

print(x)
print(y)

L1 = [2,3,4]   # L1 referes to the object list
L2= L1         # L2 refers to the same object list
L1[0]=24       # here were are not changing the object list but the content
L2[2]=30       # here were are not changing the object list but the content


print(L1)
print(L2)
print(L1==L2)

# Mutable objects can be identical in content and yet be actually different objetcs
L = [1,2,3]
M = [1,2,3]

print(M==L)         # is the content the same? True
print(M is L)       # is the object the same? False

# function ID gives the pointer number of the object
print(id(L1))
print(id(L2)) # L2 and L1 have the same ID number
print(id(M))
print(id(L))
# basically: M is L and id(M) == id(L) are the same
print(L1 is L2)
print(id(L1) == id(L2))

print(id(x))
print(id(y))


# copying objects
LL = [1,2,3]
MM = LL         # the object [1,2,3] has two names
MM = list(LL)   # we are creating a copy of the object with a diffrent name
# MM = LL[:]    # another way to create a copy of this inmutable object
print(MM == LL)          # true
print(id(MM) == id(LL))  # false

# shallow copy: constructs a new compound object and then inserts its reference into it to the original object
#       we create a copy of an compound object but the reference to the object inside the compound object are mantained.
# deep copy constructs a new compound object and then recursively inserts copies into it of the original objects
#       we create a copy of an compound object and the reference to the object inside the compound object are also changed.