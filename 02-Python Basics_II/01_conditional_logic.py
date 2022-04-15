# Conditional Logic
is_old = True
is_licensed = True

# Version 1
# you can have multiple conditions with elif

# Python is sensitive to indent

if is_old: # Sets a condition based on the expression
    print('you are old enough to drive!')
elif is_licensed: # Sets a second condition
    print('you can drive now!')
else: # If both conditions fail, then does that action
    print('you are not of age!')

print('okok')

# Version 2
# you can use expressions as 'and' or 'or' together in the if
if is_old and is_licensed: # Sets a condition based on the expression
    print('you are old enough to drive, and you have a license!')
else: # If both conditions fail, then does that action
    print('you are not of age!')

print('okok')