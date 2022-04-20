# Exercise: Check for duplicates in list
# find and print the duplicates without using set
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for item in some_list:
    if some_list.count(item) > 1: # count returns number of occurences of value in the list
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)
