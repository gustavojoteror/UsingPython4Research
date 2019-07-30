# how does pythong know which of the many function update to use?
# To make the determination the so-called scope rules are used.
# It searches for the object, layer by layer, moving from inner layers towards outer lauers, and it uses
# the first update function that finds.
# python follows the LEGB rule
#   L   Local               (current function you are in)
#   E   Enclosing function  (function that called the current function, if any)
#   G   Global              (module in which the function was defined)
#   B   Built-in            (Python's built-in namespace)

def update():
    x.append(1)


x = [1,1]
print(x)
update()        # update modifies the list x
# Python does the following:
#     1. Python tries to find x inside the scope of the function update, but it doesn't exist.
#     2. Next python looks in the next layer: enclosing function, however in this case there are no enclosing functions
#     3. Next is the globale layer does contain an object named x. This is the first object x that python finds and is therefore
# the one it will change.
# that means we can manipulate global variables (variables in the global scope) from within functions.
print(x)

print('===========================')
# next example on "Scope Rules" and Mutability and inmutability of python objects
def update(n,x):
    # local (local function)
    # n, x are the two function parameters defined when the function is also defined
    # In contrast, arguments, outside when the function is called, n and x are objects that are passed to a function as its inputs
    # Therefore, an argument is passed to a function as its input
    n=2         # this is an assigment, which create a new variable that happens to be called 'n'
    x.append(4)
    print('update: ', n , x)
    # now that python is exiting the function it will delete the local variables: n=2
    # remeber that a list is a mutable object and a number is not.

def main():
    #enclosing function
    nn = 1
    xx = [0,1,2,3]
    print('main: ', nn, xx)
    update(nn,xx)
    print('main: ', nn, xx)

#global scope
main()