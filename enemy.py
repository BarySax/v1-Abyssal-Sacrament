from bob import Bob 
from joe import Joe 
from tatie_michel import Tatie_michel
import random 


class Enemy:
    def __init__(self):
        self.type = ["joe", "bob", "tatie-michel"]
        
    def chose(self):
        self.name = random.choice(self.type)
        if self.name == "joe":
            self.joe = Joe()
            print("penis")
            

        if self.name == "bob":
            self.bob = Bob()
            print("penis")

        if self.name == "tatie-michel":
            self.tatie_michel = Tatie_michel()
            print("penis")

    def attaque(self, hp):
        self.player_hp = hp
        self.joe.attaque()
        
        return self.player_hp