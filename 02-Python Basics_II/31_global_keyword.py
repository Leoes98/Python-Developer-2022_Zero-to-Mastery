# Global Keyword

a = 10

def confusion(b): # parameters are considered local variables (can be used inside the function but not outside)
    print(b)
    a = 90

confusion(300)



# Using counter with global variables

# Method 1
# calling the global variable
total = 0

def count():
    global total # let the function know that a global variable will be used
    total += 1
    return total

print(count()) # prints 1
print(count()) # prints 2
print(count()) # prints 3

# Method 2
# using dependency injection
total = 0

def count(total):
    total += 1
    return total

print(count(count(count(total)))) # count is called three times so it returns 3
