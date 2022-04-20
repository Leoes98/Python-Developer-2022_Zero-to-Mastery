# Functions
# Allows to perform actions and use it along the code
def say_hello(): # we use 'def' to define that we are creating a function
    print('hellllooooo')

say_hello()

def get_tree():
    picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]

    for row in picture:
        for pixel in row:
            if not pixel:
                print(' ', end='')
            else:
                print('*', end='')
        print()

get_tree()
