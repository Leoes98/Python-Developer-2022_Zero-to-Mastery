# Default Parameters
# We set defaul values for the input parameters, if not called, the default values will be used
def say_hello(name = 'Darth Vader', emoji = '\U0001F608'): # This code '\U0001F608' returns a 'smiling face with horns' emoji
    print(f"helloooo {name} {emoji}")

# Keyword Arguments
say_hello(emoji='😀', name='Leo')
say_hello()

say_hello(name='Leo')
say_hello(emoji='😀')