# While Loops

# For simple loops or iterating over objects, for loops are the best
# When you are not sure how many times you need to loop, using while would be better

my_list = [1,2,3]

for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1


while True:
    response = input('say something: ')
    if (response == 'bye'):
        break
