# Formatted Strings

name = 'Johnny'
age = 55

# Without formatted strings:
print ('hi ' + name + '. You are ' + str(age) + ' years old')

# With formatted strings for Python 2:
print('hi {0}. You are {1} years old'. format(name, age))

# With formatted strings for Python 3:
print(f'hi {name}. You are {age} years old')