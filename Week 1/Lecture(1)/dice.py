import random

class Dice: # creates a class
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides) # rolls a random number between 1 and the number of sides

dice = Dice(6) # tells the class the numberof sides the dice has
for roll in range(100):
    print(dice.roll())

dice2 = Dice()
print(dice2.roll())