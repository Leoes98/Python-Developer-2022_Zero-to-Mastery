# List Slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart[-1])
print(amazon_cart[::2])
print("")

# Lists are mutable
amazon_cart[0] = 'laptop'
print(amazon_cart[:3])

new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
print("")

# If we want to copy a list, we should slice it, otherwise:
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart) # this list would also be changed
print("")

# If we just want to copy it:
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)