# Range
# makes a number iterable
for number in range(10):
    print(number)

# if variable in the loop is not needed:
for _ in range(0,10):
    print("email sent")

for i in range(5,0, -2): # range: start, finish, step
    print(i)

# Creating a list with range:
my_list = list(range(10))
print(my_list)
