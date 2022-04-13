# List Methods
basket = [1,2,3,4,5]

# adding
basket.append(100) # it just adds a new value to the list but doesn't returns it
# new_list = basket.append(100) # that would return None
new_list = basket
print(basket)
print(new_list)

# inserting
basket.insert(2, 99) # We specify the index were we want to insert the element
print(basket)

# extending
basket.extend([101, 102])
print(basket)

# pop
basket.pop()
print(basket) # removes the last item
basket.pop(0)
print(basket) # removes the item specified by the index

new_list = basket.pop()
print(new_list) # returns the element that was removed

# remove
basket.remove(3) # we give the value we want to remove
print(basket)

# clear
basket.clear()
print(basket) # removes everything in the list