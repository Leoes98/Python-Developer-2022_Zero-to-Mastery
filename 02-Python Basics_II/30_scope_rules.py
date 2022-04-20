# Scope Rules

a = 1 # assigns 1 to global variable a

def confusion():
    a = 5 # assigns 5 to local variable a inside the function
    return a

print(confusion()) # returns 5
print(a) # returns 1



###########
# Example 2
###########

a = 1 # global variable
def parent():
    b = 1 # parent local variable of confusion
    def confusion():
        c = 1 # local variable of confusion
        return sum # built in python function
    return confusion()

print(parent())
print(a)

#1 - start with local
#2 - parent local?
#3 - Global
#4 - built in python functions
