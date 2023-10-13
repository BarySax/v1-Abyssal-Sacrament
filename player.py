from dice import Dice
dice = Dice()
class Player:
    def __init__(self):
        self.inventory = []
        self.inventory_weapon = []
        self.inventory_armor = []
        self.name = str(input("Comment vous nommez-vous?\n\nReponse: "))
        self.race = int(input("A quel peuple appartenez-vous:\n1-Humain\n2-Elfe\n3-Nain\n\nReponse: "))
        self.p_class = int(input("Quel classe voulez etre:\n1-Chevalier\n2-Sorcier\n\nReponse: "))
        if self.p_class == 1:
          self.p_class = "Chevalier"
          self.inventory_weapon.append("Epee")
          self.inventory_armor.append("Armure de fer")
        else:
          self.p_class = "Sorcier"
          self.inventory_weapon.append("Baton de sorcier")
          self.inventory_armor.append("Robe de sorcier")
        if self.race == 1:
            self.stat_int = 10
            self.stat_strenght = 10
            self.stat_speed = 2
            self.stat_hp = 100
        elif self.race == 2:
            self.stat_int = 15
            self.stat_strenght = 8
            self.stat_speed = 4
            self.stat_hp = 80
        else:
            self.stat_int = 8
            self.stat_strenght = 15
            self.stat_speed = 1
            self.stat_hp = 120
        add_int = dice.lancer(1,10)
        add_strenght = dice.lancer(1,10)
        self.stat_int += add_int
        self.stat_strenght += add_strenght
        print("Vous avez:\n" + str(self.stat_int) + " point d'intelligence\n" + str(self.stat_strenght) + " point de force\n" + str(self.stat_hp) + " point de vie\n" + str(self.stat_speed) + " de vitesse de deplacement")
        print("Etant donne que vous etes un " + str(self.p_class) + " vous avez:\n" + str(self.inventory_weapon) + "\n" + str(self.inventory_armor))