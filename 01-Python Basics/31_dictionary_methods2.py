# Dictionary Methods 2
user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 22
}

# in
print('size' in user) # to check if that string is in the dictionary keys

# keys
print('greet' in user.keys()) # checks if its in the dicitonary keys

# values
print('hello' in user.values()) # checks if its in the dicitonary values

# items
print(user.items()) # returns the items of a dictionary inside a list that contains tuples of its keys and values

# copy
user2 = user.copy() # creates a copy of the dictionary
print(user2)

# clear
print(user.clear()) # creates an empty dictionary

# pop
print(user2.pop('age')) # returns the value of the key that it removes
print(user2)

# pop item
print(user2.popitem()) # randomly removes an item
print(user2)

# update
print(user2.update({'basket': 55})) # updates a value given its key, if the key doesn't exist it creates a new one
print(user2)
