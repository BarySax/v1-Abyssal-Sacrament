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
            self.joe.attaque()

        if self.name == "bob":
            self.bob = Bob()
            print("penis")
            self.bob.attaque()

        if self.name == "tatie-michel":
            self.tatie_michel = Tatie_michel()
            print("penis")
            self.tati_michel.attaque()
        
        