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

        print("tu combat", chance)

    def printDist(self):
        print("Votre distance avec l'ennemi est de:\n" +str(self.distBetweenCharac) + " metre")
        print("vos hp", self.player_hp)
        print("hp de lenemy", self.enemy.hp)

    #attaque de lenemy
    def tourEnemy(self):
        #variable de fonction
        attaque = self.enemy.attaque()
        

        #attaque de lenemy
        if attaque == 1:
            #attaque de bob
            if self.enemy.fire:
                self.player_hp -= self.enemy.strenght
                print("lenemy attaque -" + str(self.enemy.strenght) + "hp")

            else:
                if self.distBetweenCharac <= 3:
                    self.player_hp -= self.enemy.strenght
                    print("lenemy attaque -"+ str(self.enemy.strenght)+"hp")

                else:
                    self.distBetweenCharac -= self.enemy.speed
                    print("lenemy avance")

        #ennemy recule
        elif attaque == 2:
            self.distBetweenCharac += self.enemy.speed
            print("leney recule")

        #lenemy avance
        elif attaque == 3:
            self.distBetweenCharac -= self.enemy.speed
            print("lenemy avance")

    def tourPlayer(self):
        self.choix = int(input("Que voulez vous faire:\n1-Attaquer\n2-Utiliser un objet (pas encore disponible)\n3-avancer\n4-reculer\n5-fuir\n\nReponse: "))
        if self.choix == 1:
            
            if self.player_inventory_weapon == "Épée":
                if self.distBetweenCharac <= 3:
                    self.enemy.hp -= self.player_strenght
                    print("Vous attaquez -"+str(self.player_strenght)+"hp")
                else :
                    print("vous etes trop loin")
                    print("vous avancez")
                    self.distBetweenCharac -= self.player_speed

            else:
                print("vou navez pas d'arme approprier")

        elif self.choix == 3:
            print("vous avancez")
            if self.distBetweenCharac <= 0:
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
        

