# is vs ==

print("==:")
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([1,2,3] == [1,2,3])

# is
# is goes to the memory allocation to see if both values are equal
print("\nis:")
print(True is True)
print(True is 1)
print('' is 1)
print([] is 1)
print([] is []) # Returns False because each list has its own space in memory
print(10 is 10.0)
print([1,2,3] is [1,2,3])

a = [1,2,3]
b = [1,2,3]
print(a == b) # just looks the values
print(a is b) # is more strict