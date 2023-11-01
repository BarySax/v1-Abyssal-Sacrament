import random

class Tatie_michel:
    def __init__(self):
        self.hp = 100
        self.strenght = 20
        self.speed = 4
        self.fire = False
        self.flying = True
    
    def attaque(self):
        return random.randint(1,3)