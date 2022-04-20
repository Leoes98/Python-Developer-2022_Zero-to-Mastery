# Walrus Operator

# New in python 3.8: walrus (:=)
# New syntax [:=] that "assigns values to variables as part of a larger expression"
# Source: https://docs.python.org/3/whatsnew/3.8.html

a = "hellooooooooo"

if ((n:=len(a)) > 10):
    print(f"Too long {n} elements")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)
