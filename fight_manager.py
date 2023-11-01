from player import Player
from tatie_michel import Tatie_michel
from joe import Joe
from bob import Bob
import random


#initialization des classe

class FightManager:
    def __init__(self):

        #variable de la fonction
        chance = random.randint(0,3)
        
        #variable de la classe
        self.distBetweenCharac = 5
        

        #choix ennemy
        if chance == 0:
            self.enemy = Joe()
        
        elif chance == 1:
            self.enemy = Bob()
        
        elif chance == 3:
            self.enemy =  Tatie_michel()
        
        self.player = Player()

    def printDist(self):
        print("P,", str(self.distBetweenCharac) + "m", ", E")
        
    #attaque de lenemy
    def tourEnemy(self):
        #variable de fonction
        attaque = self.enemy.attaque()

        #attaque de lenemy
        if attaque == 1:
            #attaque de bob
            if self.enemy.fire:
                self.player.stat_hp -= self.enemy.strenght
                print("lenemy attaque -" + self.enemy.strenght + "hp")

            else:
                if self.distBetweenCharac <= 3:
                    self.player.stat_hp -= self.enemy.strengh
                    print("lenemy attaque -"+self.enemy.strenght+"hp")

                else:
                    self.distBetweenCharac -= 1
                    print("lenemy avance")

        #ennemy recule
        elif attaque == 2:
            self.distBetweenCharac += 1

        #lenemy avance
        elif attaque == 3:
            self.distBetweenCharac -= 1

    def tourPlayer(self):
        self.player.attaque()

