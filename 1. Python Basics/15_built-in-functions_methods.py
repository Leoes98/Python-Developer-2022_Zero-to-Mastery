# Built-In Functions
# more info: https://docs.python.org/3/library/functions.html
greet = 'hellloooo'
print(greet[0:len(greet)])

# Built-In Methods
# more info for string methods: https://www.w3schools.com/python/python_ref_string.asp
quote = 'to be or not to be'
print(quote.upper()) # upper cases everything
print(quote.capitalize()) # capitalizes the string
print(quote.find('be'))  # finds first occurence of the substring
print(quote.replace('be', 'me')) # replaces every ocurrence of the old substring by the new one

print(quote) # Strings are immutable so the changes made by the methods won't be saved
# If we want to save the changes we need to create another variable
quote2 = quote.replace('be', 'me')
print(quote2)
