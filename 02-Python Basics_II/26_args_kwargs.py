# *args and **kwargs

# *args accepts any number of arguments you give and store them as tuple

# **kwargs accepts keywords arguments and aggregates them into a dictionary

def super_func(name, *args, i='hi', **kwargs):
    print(*args)
    print(kwargs) # it's stored as a dictionary
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total

print(super_func('Andy', 1,2,3,4,5, num1=1, num2=10))
