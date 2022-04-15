# Enumerate
# Returns the index and value of the items
# useful if you need an index counter
for i,char in enumerate('Helllooo'):
    print(i, char)

# Just print the index of the number 50 on the list
for i, number in enumerate(list(range(100))):
    if number == 50:
        print(f'index of 50 is: {i}')
