from player import Player
from tatie_michel import Tatie_michel
from joe import Joe
from bob import Bob
import random


#initialization des classe

class FightManager:
    def __init__(self, player_hp, player_strenght, player_speed, player_inventory_weapon):

        #variable de la fonction

        chance = random.randint(0,2)
        
        #variable de la classe
        self.distBetweenCharac = 5
        self.player_hp = player_hp
        self.player_strenght = player_strenght
        self.player_speed = player_speed
        self.player_inventory_weapon = player_inventory_weapon
        
        


        #choix ennemy
        if chance == 0:
            self.enemy = Joe()

        elif chance == 1:
            self.enemy = Bob()

        
        elif chance == 2:
            self.enemy =  Tatie_michel()
        

    def printDist(self):
        print("Votre distance avec l'ennemi est de:\n" +str(self.distBetweenCharac) + " metre")

    #attaque de lenemy
    def tourEnemy(self):
        #variable de fonction
        attaque = self.enemy.attaque()

        #attaque de lenemy
        if attaque == 1:
            #attaque de bob
            if self.enemy.fire:
                self.stat_hp -= self.enemy.strenght
                print("lenemy attaque -" + self.enemy.strenght + "hp")

            else:
                if self.distBetweenCharac <= 3:
                    self.stat_hp -= self.enemy.strengh
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
        self.choix = int(input("Que voulez vous faire:\n1-Attaquer\n2-Utiliser un objet (pas encore disponible)\n3-avancer\n4-reculer\n5-fuir\n\nReponse: "))
        if self.choix == 1:
            if self.enemy.flying:
                if self.player.inventory_weapon == "Serment de vérité":
                    self.enemy.hp -= self.player.stat_strenght
                    print("Vous attaquez -"+self.player.stat_strenght+"hp")
                else:
                    print("vou navez pas d'arme approprier pour un enemie volant")

            else:
                if self.player_inventory_weapon == "Épée":
                    if self.distBetweenCharac <= 3:
                        self.enemy.hp -= self.player.stat_strenght
                        print("Vous attaquez -"+self.player.stat_strenght+"hp")
                    else :
                        print("vous etes trop loin")
                        print("vous avancez")
                        self.distBetweenCharac -= self.player_speed

                else:
                    print("vou navez pas d'arme approprier")

        elif self.choix == 3:
            print("vous avancez")
            self.distBetweenCharac -= self.player_speed

        elif self.choix == 4:
            print("vous reculez")
            self.distBetweenCharac += self.player_speed

    def fight(self):
        print("vous avez "+str(self.player_hp)+"hp")
        while self.player_hp > 0 and self.enemy.hp > 0:
            self.printDist()
            self.tourEnemy()
            self.tourPlayer()
        
        if self.player_hp > 0:
            return True

        else:
            return False
        

