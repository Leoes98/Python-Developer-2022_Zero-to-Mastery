# Exercise: Type Conversion
# Build a program that guesses your age by the year you were born
birth_year = input('What year were you born? ')

age = 2022 - int(birth_year) # Input return string data type so we have to convert it into int
print(f'Your age is: {age}')


# Bonus: What if we run this code in another year?
import datetime # We first import a Python package to get the time
now = datetime.datetime.now() # We set the present time

present_year = now.year
age = present_year - int(birth_year)
print(f'Your age is: {age}')
