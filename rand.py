import random

class dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,5)
        return first, second


dice1 = dice()
print(dice1.roll())