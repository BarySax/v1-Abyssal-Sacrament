from player import Player
from flyer import Flyer
from runner import Runner
from launcher import Launcher
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
            self.enemy = Runner()
        
        elif chance == 1:
            self.enemy = Launcher()
        
        elif chance == 3:
            self.enemy =  Flyer()
        
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
                    self.distBetweenCharac -= self.enemy.speed
                    print("lenemy avance")

        #ennemy recule
        elif attaque == 2:
            self.distBetweenCharac += self.enemy.speed

        #lenemy avance
        elif attaque == 3:
            self.distBetweenCharac -= self.enemy.speed

    def tourPlayer(self):
        choix = self.player.attaque()
        if choix == 1:
            if self.enemy.flying:
                if self.player.inventory_weapon == "Serment de vérité":
                    self.enemy.stat_hp -= self.player.stat_strenght
                    print("Vous attaquez -"+self.player.stat_strenght+"hp")
                else:
                    print("vou navez pas d'arme approprier pour un enemie volant")
            
            else:
                if self.player.inventory_weapon == "Épée":
                    if self.distBetweenCharac <= 3:
                        self.enemy.stat_hp -= self.player.stat_strenght
                        print("Vous attaquez -"+self.player.stat_strenght+"hp")
                    else :
                        print("vous etes trop loin")
                        print("vous avancez")
                        self.distBetweenCharac -= self.player.speed

                else:
                    print("vou navez pas d'arme approprier")

        elif choix == 3:
            print("vous reculez")
            self.distBetweenCharac += self.player.speed

        elif choix == 4:
            print("vous avancez")
            self.distBetweenCharac -= self.player.speed

    def fight(self):
        while self.player.stat_hp > 0 and self.enemy.stat_hp > 0:
            self.printDist()
            self.tourEnemy()
            self.tourPlayer()
