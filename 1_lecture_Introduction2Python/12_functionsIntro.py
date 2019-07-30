# statement: def is used for defining an function
# statement: return results object that will send back the functions

def add(a, b):      # def statement creates an object and assigns it to a name (in this case add)
    # local variables: variables only possible to change inside the function
    sum =  a + b
    return sum


def add_and_sub(a, b):
    # local variables: variables only possible to change inside the function
    sum  =  a + b
    diff =  a - b
    return (sum, diff)  # this is a tuple

def modify(mylist):
    mylist[0] *=10


print(add(10,2))            # inside the function: a=10 and b=2 (functions match by position

print(add_and_sub(20,15))   # python returns a tuple

print(add)
newadd=add          # we can reassing the name of the function if we want
print(newadd(5,8))

# lets use now inmutable objects!
L = [1,3,5,6,8]
print(L)
modify(L)
print(L)