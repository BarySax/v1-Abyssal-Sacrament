import random

class Joe:
    def __init__(self):
        self.hp = 100
        self.strenght = 10
        self.speed = 4
        self.fire = False
        self.flying = False

    def attaque(self):
        return random.randint(1,3)