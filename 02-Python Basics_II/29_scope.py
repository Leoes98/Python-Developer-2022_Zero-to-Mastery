# Scope - what variables do I have access to?

if True:
    x = 10 # this is part of the global variables

def some_func():
    total = 100 # variable defined inside some function isn't part of the global scope

#print(total) # would give error
