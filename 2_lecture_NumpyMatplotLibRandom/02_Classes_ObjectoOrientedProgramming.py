################
# classes and Object Oriented programming
# objects consists of both internal data and methods that perform operations on the data.
# a class is a new object type you create: with internal data and methods

# Inheritance
# this new object type can inherent. Inheritance means that you can define a new object type (a new class)
# that inherits properties from an existing object type.

class MyList(list):     # the name of the new object (in this case MyList) immediately follow the word: "class"
                        # Notice that we placed parentheses after MyList. This is how Python specifies inheritance.
                        # so in this new class that inherits from list I can redefine or add any attribute/new attribute
                        # class DerivedClassName(BaseClassName):
                        # this specific class is initialized with a list

    # def __init__(self):
        ### empty


    # instance methods that operate on an instance of the class.
    # by convention the name of the class instance is called "self" and it is always passed as the first argument
    def remove_min(self):
        self.remove(min(self))

    def remove_max(self):
        self.remove(max(self))


x = [10, 4, 6, 8, 12, 53, 1, 4, 6, 7, 3, 2]
y = MyList(x)

print(dir(x))
print(' ')
print(dir(y))       #two extra methods are printed: remove_max, remove_min
print(' ')
print(y)
y.remove_min()  # 1 is removed from the list
print(y)
y.remove_max()  # 53 is removed form the list
print(y)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# more info on python classes
# from: https://docs.python.org/3/tutorial/classes.html
#  1. normally class members (including the data members) are public (except see below Private Variables), and all member functions are virtual.
#  2. When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace.
#        In particular, function definitions bind the name of the new function here.