# Short Circuiting

# It helps Python be more efficient by stopping any operation its doing if the condition is not met.
# For example if while using 'OR': the first term is True, it doesn't needed to go through the second term.
# Same if using 'AND': if the first term is False, no need to go through the second operation.
# So it stops or go to the next section, and saves computational power

is_Friend = True
is_User = True

if is_Friend or is_User:
    print('best friends forever')