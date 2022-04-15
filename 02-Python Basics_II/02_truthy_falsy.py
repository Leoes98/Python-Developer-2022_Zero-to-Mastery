# Truthy vs Falsy

# some values can return True or False if they are Truthy of False
# For example: bool(0) or bool('') return False
# While bool(1) or bool('hi') return True
password = '123'
username = 'johnny'

if password and username:
    print('You have your password and username saved')