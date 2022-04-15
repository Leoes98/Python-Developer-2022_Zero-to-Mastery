# For Loops
# Allows to run python code over and over again

# Using Strings
print("Strings:")
for item in 'Zero to Mastery': # item could be any variable
    print(item)

# Using List
print("\nList:")
for item in [1,2,3]: # item could be any variable
    print(item)

# Using Tuple
print("\nList:")
for item in (1,2,3): # item could be any variable
    print(item)

# Using Set
print("\nSet:")
for item in {1,2,3}: # item could be any variable
    print(item)

# Loop inside another
print("\nTwo Loops:")
for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)
