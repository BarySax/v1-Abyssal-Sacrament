import random

class Launcher:
    def __init__(self):
        self.hp = 100
        self.strenght = 10
        self.speed = 2
        self.fire = True
        self.flying = False
    
    def attaque(self):
        return random.randint(1,3)
