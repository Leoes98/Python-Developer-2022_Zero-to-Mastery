# Docstrings
# uses to give information about the functions we create

def test(a):
    '''
    Info: this functions tests and prints param a
    '''
    print(a)

test('!!!')

help(test) # prints the docstring

print(test.__doc__) # Also prints docstring but using a magic method
