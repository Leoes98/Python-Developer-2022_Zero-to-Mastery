# Dictionary Methods
user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 22
}

# get
print(user.get('age', 24)) # It is used to know if the dictionary has a key and get its value, you can also add a default value

# Create dictionary method 2
user2 = dict(name = 'John')
print(user2)
