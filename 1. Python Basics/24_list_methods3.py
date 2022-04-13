# List methods
basket = ['a','b','x','c','d','e']

# Sort
basket.sort() # method
print(basket)

basket = ['a','b','x','c','d','e']
print(sorted(basket)) # built-in function that creates a new sorted list
print(basket)

# another way to copy a list:
new_basket = basket.copy()
print(new_basket)

# Reverse
basket.sort()
basket.reverse() # reverses element list
print(basket)