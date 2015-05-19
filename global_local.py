__author__ = 'shannon'

# Here x is not a global variable.
x = 6


def example():
    z = 5
    print(z)
    print(x+5)

    ''' x += 6
    this will return an error because x is not a global variable
    we can access x but we can't modify it
    A solution is to make x global or use another variable & return it
    '''


def example2():
    global x
    print(x)
    x += 5
    print(x)


# The good solution.

def example3():
    globx = x
    print('variable globx', globx)
    globx += 5
    print('variable globx avec pre incrementation', globx)

    return globx

# Functions call.

example()
example2()
example3()

# Get variable value with a function return.

getGlobx = example3()
print('Globx with a return function', getGlobx)