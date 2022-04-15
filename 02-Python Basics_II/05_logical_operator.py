# Logical Operators
# or, and, < , >, ==
print(4 < 5)
print(4 > 5)
print(4 == 5) # needs double =, one is used to assign values to a variable

print('a' > 'b') # returns False
print('a' > 'A') # return True

'''
It is because Python compares the characters by converting it into integers according to ASCII Table
Source: https://www.asciitable.com/

So 'a' is 97 decimal, 'b' is 98, and 'A' is 65
'''
print(ord('a'))
print(ord('b'))
print(ord('A'))

print(1 >= 0) #greater than or equal to
print(1 <= 0) #less than or equal to

print(1 != 0) # not equal to

print(not(True)) # does the contrary
