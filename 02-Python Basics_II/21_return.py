# Return

# Functions either return something or modifies the code

def say_hi():
    print('hii') # modifies

def sum(num1, num2):
    return num1 + num2 # returns

total = sum(10,5)
print(sum(4,total))

# A functions should:
# 1. do one thing really well
# 2. return something

def sum2(num1, num2):
    def another_func(n1, n2):
        return n1 + n2 # this part actually return the sum
    return another_func(num1, num2) # return is used to call the nested function
    return 5 # this won't work, as soon as it looks at the first return it exits the function
total = sum(10, 20)
print(total)
