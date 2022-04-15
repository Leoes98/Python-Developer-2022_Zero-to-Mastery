# Tuple
my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:4]

print(new_tuple)

x,y,z, *other = (1,2,3,4,5)
print(other)

# Count
print(my_tuple.count(5)) # counts number of elements in tuple

# Index
print(my_tuple.index(5)) # returns the index where the element is in the tuple

# Len
print (len(my_tuple)) # returns length of tuple