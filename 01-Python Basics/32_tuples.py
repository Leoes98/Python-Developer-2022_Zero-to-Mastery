# Tuple
# Immutable lists
# can be used to tell programmer that it shouldn't be changed
# are usually faster that working with lists
my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

user = {
    (1,2): [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user[(1,2)]) # a tuple can be used as dictionary key because its immutable