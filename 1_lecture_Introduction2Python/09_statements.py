##
# return statement is used to return vakues from a function
# import statement use to import modules
# pass statement used to do nothing

# compound statements (multiples clauses)
#       statement:
#           codes.... #indent needed
#
# examples: if, for, while, try
# indentation in pyton is not cosmetic it is important
x =5
y = 10
if x > y:
    absval = x-y
    print('x>y')
elif y > x:
    absval = y-x
    print('y>x')
else:
    absval = 0
    print('0')

##### loops
for x in range(10):
    print(x)

# pythonic and not pythonic for loops
names = ['Jim', 'Tom', 'Gis', 'Gus']
print(names)
for i in names:  # the pythonic way
    print(i)
print(names)
for i in range(len(names)): # not very pythonic
    print(names[i])

age = {"Tim": 29,   "Gus": 31, "Daniela": 29, "Ximena": 6, "Fini": 69}

for name in age.keys():
    print(name, age[name])  # here we are using both posibilities

# same as it is above because it is a ditionary
for name in age:
    print(name, age[name])

print("  ")
for name in sorted(age.keys()):
    print(name, age[name])  # now the dictionary is sorted alphabetically
print("  ")
for name in sorted(age.keys(), reverse=True):
    print(name, age[name])  # now the dictionary is sorted reverse alphabetically