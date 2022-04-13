# Dictionary
# Uses a key (which can be any data type) to wrap some elements
dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'c': True
}

print(dictionary['b'])
print(dictionary['a'][1])

# We can add a dictionary into a list
my_list = [
    {
    'a': [1,2,3],
    'b': 'hello',
    'c': True
    },
    {
    'a': [4,5,6],
    'b': 'bye',
    'c': False
    }
]

print(my_list[0]['a'][2])
