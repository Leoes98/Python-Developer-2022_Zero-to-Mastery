# String indexes

selfish = 'me me me'
        # 01234567

print(selfish[0])
print(selfish[7])

# [start:stop]
val = '01234567'
print(val[0:8])
print(val[1:])
print(val[:5])
print(val[-1])

# [start:stop:stepover]
val = '01234567'
print(val[0:8:2])
print(val[::2])
print(val[::-1])