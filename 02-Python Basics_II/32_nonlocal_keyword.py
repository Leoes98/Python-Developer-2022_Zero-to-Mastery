# Nonlocal Keyword

def outer():
    x = "local"
    def inner():
        nonlocal x  # it will use x as a nonlocal variable, instead of creating a local variable it uses the parent function variable
        x = "nonlocal" # variable x is changed not only in inner, but also in outer
        print("inner", x)

    inner()
    print("outer:", x)

outer()

# Scope is useful to understand the value of saving memory between global, local, and parent variables. 
# Instead of using everything in global variables, memory could be saved if using wisely inside functions for example.
