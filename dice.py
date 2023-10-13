import random

class Dice:
    def __init__(self):
        self.num = 0
    
    def lancer(self, num_dice, face):

        for i in range(num_dice):
            result = random.randint(1,face)
        return result