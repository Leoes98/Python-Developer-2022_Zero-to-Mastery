# Iterables

# iterable: list, dictionary, tuple, set, string
# iterate: one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

print("Dictionary items:")
for item in user.items():
    print(item)

print("\nDictionary values:")
for item in user.values():
    print(item)

print("\nDictionary keys:")
for item in user.keys():
    print(item)

print("\nKeys and Values separate:")
for key, value in user.items():
    print(f"Key: {key}, Value: {value}")
