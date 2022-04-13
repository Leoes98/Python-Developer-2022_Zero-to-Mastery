# Exercise: Password Checker
username = input('Username: ')
password = input('Password: ')

password_length = len(password)
hidden_pass = '*' * password_length

print(f'{username}, your password, {hidden_pass}, is {password_length} characters long')
