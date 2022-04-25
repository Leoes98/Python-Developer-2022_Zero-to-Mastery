# OOP
class PlayerCharacter:
    def __init__(self, name, age): # constructor method
        self.name = name #attributes of the object
        self.age = age
    
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 44) # Creates the object, needs the inputs in the constructor method
player2 = PlayerCharacter('Tom', 21)

print(player1.name)
print(player2.name)
print(player2.run())

# The objects live in different places in memory
player1.attack = 'punch'

print(player1.attack)
#print(player2.attack) # returns error because it was only created on player1
