# Break, Continue, Pass
my_list = [1,2,3]

print("Break:")
# stops the loop
while True:
    print("hi!")
    break

print("\nContinue:")
# continue will make the program move to the next iteration, so nothing will get printed
for item in my_list:
    continue 
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue

print("\nPass:")
# moves on with the code, useful when still not sure about what to do inside the loop but want to run the whole code
for item in my_list:
    # thinking about it
    pass