# Set
# unordered collections of unique objects
# there is no duplicates
my_set = {1,2,3,4,5,5}
print(my_set)

my_set.add(100)
my_set.add(2)
print(my_set)

my_list = [1,2,3,4,5,5]
print(set(my_list)) # to delete the duplicates on list
print(list(set(my_list))) # to get back the list

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)