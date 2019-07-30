# three is a collection of objects by their position:
#       lists
#       tuple
#       range objects
# indexing start in 0
# s= [1    ,2    ,5    ,9    ,10]
#     s[0] ,s[1] ,s[2] ,s[3] ,s[4]
#     s[-5],s[-4],s[-3],s[-2],s[-1]
# slicing
#       s[2:4]  {start position:stop position]
#           this will include s[2], 2[3]
#           s[4] is not included

s=[1,2,5,9,10]
print(s)
print(s[0])
print(s[-1])
print(s[-5])
print(s[2:4])

#########################################################################
#           LISTS   LISTS   LISTS   LISTS   LISTS   LISTS   LISTS
## lists: mutable sequeucen of object of any type (store homogeneous items
#               a string can be seen as a list of characters (only characters)
#               However strings are immutable while list aren't
print(dir(list)) #check all the attributes available of a list
s.append(100)
print(s)
s[-1]-=10
print(s)

b = [12,14,15]  # this will concatenated the lists
print(s+b)
print(type(s))     # type list
print(type(s[0]))  # type integer
print(list)        # help for list

# list method
number = [1,3,14,7,70,9,19]
print(number)
print(number.reverse())   #this doesn't return any object, this just changed the object
print(number)
number.sort()
print(number)

names = ["Zofia", "Ramon", "Alvaro", "Gustavo"]
print(names)
names.sort()
print(names)
names.reverse()


print(names)
print(sorted(names) )  #this is a function that return the input list sorted
print(len(names) )     #this is a function that return the input list's length

#########################################################################
#           TUPLES   TUPLES   TUPLES   TUPLES   TUPLES   TUPLES   TUPLES
## TUPLES: inmutable sequence typically used to store heterogeneous data.
# useful to return from a function
print(dir(tuple)) #check all the attributes available of a tuple
T= (1,2,4,5,6)
print(len(T))
print(T + (1502,58))
print(T[1])
x = 12.23
y = 23.34

coordinate = (x , y)            #tuple packing
print(type(coordinate))
(c1, c2) = coordinate           #unpacking a tuple
print(c1)
print(type(c2))                 #type float
#########################################################################
# list inside a tuple
x_vect = [1.23, 12.3, 123]
y_vect = [23, 3, 12]
coord = (x_vect, y_vect)  #tuple of list
print(coord)
(v1, v2) = coord           #unpacking a tuple
print(type(v1))
print(v2)
#########################################################################
# tuples inside a list
a = (0,0,3)
b = (1,6,4)
c = (2,5,76)
d = (3,4,3)
coordinates= [a, b, c, d]
print(coordinates)
print(type(coordinates))
print(type(coordinates[0]))

for (x1,y1,z1) in coordinates:
    print(x1,y1,z1)

### define a tuple with a single object
coor = (2,)     # coord=(2) would be a type integer
print(type(coor))
#########################################################################
#           RANGES   RANGES   RANGES   RANGES   RANGES   RANGES   RANGES
## RANGES: inmutable sequence tof integers.
# useful for for loop
print(dir(range)) #check all the attributes available of a range
ran=range(5)  # python stops before achieving the stopping value
print(range(5))
print(type(range(5)))
# you can turn a range into a list
ran = list(ran)
print(ran)
print(type(ran))

rang= range(0,13,2)  #range(start,stop, step)
print(rang)
