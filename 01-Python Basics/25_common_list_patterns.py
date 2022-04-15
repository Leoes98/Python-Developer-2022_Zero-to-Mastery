# Common List Patterns
basket = ['a','b','x','c','d','e']

basket.sort()
basket.reverse()
print(basket[::-1]) # returns a new list with reversed element order
print(basket)

# Range
print(list(range(1,100))) # we use range to generate a list from the start and end values specified

# Join
sentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJO']) # Combines a list into a string
print(sentence)
