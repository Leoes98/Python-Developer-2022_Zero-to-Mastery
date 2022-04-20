# Clean Code

# Not clean code
print("Not clean code:")
def is_even(num):
    if num%2 == 0:
        return True
    elif num%2 != 0:
        return False

print(is_even(50))

# Clean Code
print("\nClean code:")
def is_even_clean(num):
    return num%2 == 0

print(is_even(50))
