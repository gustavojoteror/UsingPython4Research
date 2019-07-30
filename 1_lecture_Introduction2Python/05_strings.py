#########################################################################
#           STRINGS   STRINGS   STRINGS   STRINGS   STRINGS   STRINGS   STRINGS
## STRINGS: inmutable sequence of CHARACTERS.

s = "Python"
print(len(s))
print(s[0])
print(s[-1])
print(s[0:3])       # slice
print(s[-3:])       # slice, last three characters
print("y" in s)     #True
print("Y" in s)     #False

# polymorphism
print(2+2)                  # Addition
print("hello "+"world")     # Cocatenation
print(3*"hey ")             # Cocatenation= "hey "+"hey "+"hey "

#print("eight equals: "+8)             # ERROR: because you can't sum different objects
print("eight equals: "+ str(8))        # We converted the number into a string

print(dir(str))     #check all the attributes available of a string

# replace method
name = "Tina Fey"
print(name)
name2=name.replace("T", "t")  # remeber string are inmutable objects
print(name2)

# split method
names = name.split(" ") # it returns a list of strings
print(type(names))
print(len(names))
print(names)
print(names[0])
print(type(names[1]))
print(names[1].upper())  # we can apply string method to each element of the list



