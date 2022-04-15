# Our First GUI

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# 1. Iterate over the picture
# 2. if 0 -> print ' ' ; if 1 -> print *

for row in picture:
    for pixel in row:
        if not pixel:
            print(' ', end='')
        else:
            print('*', end='')
    print()
