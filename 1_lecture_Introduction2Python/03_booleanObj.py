

print(type(True))
print(type(False))  # the word true and false are taken as boolean object for python
#print(type(false))  # False need to have the first letter capitalize, if not python doesnt takes it as an unknown variable

# Only three boolean operation: or, and, not

# or operator: only one needs to be true
print(False or True)    #True
print(True or True)     #True
print(False or False)   #False
# and operator: noth need to be true
print(False and True)   #False
print(True and True)    #True
print(False and False)  #False
# not operator: negates the statement
print(not True)         #False
print(not False)        #True

# comparing
print(5 < 2)    #False
print(5 >= 2)   #True
print(5 == 2)   #False
print(5 != 2)   #True

print([2,3] == [3,2])   #False
print([2,3] == [2,3])   #True

# is comparison (compare if two object are the same)
print([2,3] is [2,3])   #False
print([2,3] is [3,3])   #False
a=[2,3]
b=a
print(a is b)   #True
b=[1,2]
print(a is b)   #False
a=b
print(a is b)   #True