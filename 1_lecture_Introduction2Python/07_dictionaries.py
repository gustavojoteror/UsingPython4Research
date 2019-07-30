##################
# dictionaries dictionaries dictionaries dictionaries dictionaries dictionaries
# are mappings from key objects to value objects
# consist of Key:Value (pairs)
# where the key is inmutable and the value can be anything
# dictionaries are mutable so they can be change once you create them
# importance:
#       perform fast lookups on unordered data.
# note: dictionaries are not sequence, therefore do not maintain any order
# therefore they have an arbitrary order.
#
#       key1 : value1
#       key2 : value2
#       key4 : value4
# each key will always go with the corresponding value
# the other of the keys are not defined

# THERE IS NO LEFT OR RIGHT ORDER IN A DICTIONARY!
# wHEN YOU ACCESS YOUR DICTIONARY MAKE SURE YOU KNOW THE TYPE OF YOUR KEY OBJECTS

print(dir(dict))    #check all the attributes available of a set
age = {}        # empty dictionary
age = dict()    # empty dictionary
age = {"Tim": 29,   "Gus": 31, "Daniela": 29, "Ximena": 6, "Fini": 69}
##     key1: val1, key2: val2, key3: val3
print(age["Gus"])       # we find the value of the given key
age["Tim"] = age["Tim"] + 1
age["Fini"] -= 1
print(age["Tim"])       # we find the value of the given key
print(age["Fini"])       # we find the value of the given key

# let check some methods of dictionary
names = age.keys()
ages  = age.values()
print(type(names))
print(names)
age["Tomas"] = 50
print(names)
print(ages)
print(age)

names = age.keys()
ages  = age.values()
print(names)
print(ages)

print("Tim" in age)  # object membership
print("Zofia" in age)  # object membership