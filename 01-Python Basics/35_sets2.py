# Sets
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# Difference
# shows the difference between two sets
print('\nDifference:')
print(my_set.difference(your_set))

# Discard
# removes an element of the set
print('\nDiscard:')
print(my_set.discard(5))
print(my_set)

#  Difference Update
# Updates the set so that the difference is removed
print('\nDifference Update:')
print(my_set.difference_update(your_set))
print(my_set)

# Intersection
# Returns the intersection between sets
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print('\nIntersection:')
print(my_set.intersection(your_set))
print(my_set & your_set) # works the same

# isdisjoint
# Returns True if the sets have nothing in common
print('\nIsdisjoint:')
print(my_set.isdisjoint(your_set))

# Union
# unite sets and removes duplicates
print('\nUnion:')
print(my_set.union(your_set))
print(my_set | your_set) # works the same

# issubset
# Returns True is the set is a subset of the other set
print('\nissubset:')
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.issubset(your_set))

# issuperset
# Returns True if the set encompasses the other set
print('\nissuperset:')
print(your_set.issuperset(my_set))