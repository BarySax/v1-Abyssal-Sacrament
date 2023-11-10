from dice import Dice
from weapon import Weapon
from armor import Armor
import time

dice = Dice()
class Player:
  def __init__(self):
    self.inventory = []

  def create_player(self):

    self.inventory = []
    self.inventory_weapon = ["Rien"]
    self.inventory_armor = ["Rien"]

    #aficher le debut de lhistoir
    print("bienvenue dans:")
    print("   db    8888Yb Yb  dP .dPY8 .dPY8      db    88         .dP-Y8    db     dP--b8 88--Yb    db    8b    d8 888888 88b 88 888888 ")
    print("  dPYb   88__dP  YbdP   Ybo.   Ybo.    dPYb   88          Ybo.    dPYb   dP      88__dP   dPYb   88b  d88 88__   88Yb88   88   ")
    print(" dP__Yb  88  Yb   8P   o. Y8b o. Y8b  dP__Yb  88  .o     o. Y8b  dP__Yb  Yb      88 Yb   dP__Yb  88YbdP88 88     88 Y88   88   ")
    print("dP    Yb 88oodP  dP    8bodP' 8bodP' dP    Yb 88ood8     8bodP  dP    Yb  YboodP 88  Yb dP    Yb 88 YY 88 888888 88  Y8   88   \n\n\n")

    print("Comme tout les soir, vous rejoigner votre lit, mais etrangement, une sensation de douleur sempare de votre corps, vous avez limpression que des main ardente vous aggrippe")
    time.sleep(2)
    print("Votre corps ce fauxant soutenir est lever dans le ciel")
    time.sleep(1.5)
    print("Puis tous dun copu vous etes projeter dans une obscuriter totale, vous voyez mainteant les main de feu vous aggriper")
    time.sleep(1.5)
    print("Les main ce reffroidise puis seffrite et tombe en poussiere")
    time.sleep(1.5)
    print("Devant vous une lumiere apparait, une lumiere dans les tenebres, une oeil yant sois meme a linterieur, le processus repliquer a l'infini")
    time.sleep(1.5)
    print("Vous savez quesque ces, ces le dieu absolue, de linfinie, leveillement")
    time.sleep(1.5)
    print("Du centre de sa sainte pupille, un sang mate sechappe et enroule votre corps vous retrouver entierrement dans une marre de sang")
    time.sleep(1.5)
    print("Une voix surgie dans votre tete, un immense honneur vous ait accorder: « Tu est le saint choisi, tu doit purger la vermines de ce monde, repond a la prophetie, et tu pourras me rejoindre dans les ABYSSE SACREMENTAL\n\n\n\n")
    time.sleep(2)

    #la chute du personage
    for i in range(10):
      print("vous tombez et tous devien sombre")
      time.sleep(1)

    print("vous vouz reveillez dans votre lit en sueur apres une longue nuit de someil dificile.")
    print("durant cette nuit vous avez eu une elumination.\n\n")

    self.name = str(input("Comment vous nommez-vous?\n\nReponse: "))
    self.race = int(input("A quel categorie appartenez-vous:\n1-Sans dessein\n2-Religieux\n3-Noble\n\nReponse: "))
    self.p_class = int(input("Quel classe voulez etre:\n1-Chevalier\n2-Inquisiteur\n\nReponse: "))
    print(self.p_class)
    if self.p_class == 1:
      self.p_class = "Chevalier"
      self.inventory_weapon.append("Épée")
      self.inventory_armor.append("Armure de fer")
    else:
      self.p_class = "Inquisiteur"
      self.inventory_weapon.append("Serment de vérité")
      self.inventory_armor.append("Habit d'inquisiteur")

    if self.race == 1:
      self.race = "Sans dessein"
      self.stat_faith= 10
      self.stat_strenght = 10
      self.stat_speed = 2
      self.stat_hp = 100
    elif self.race == 2:
      self.race = "Religieux"
      self.stat_faith = 15
      self.stat_strenght = 8
      self.stat_speed = 2
      self.stat_hp = 80
    else:
      self.race = "Noble"
      self.stat_faith = 8
      self.stat_strenght = 15
      self.stat_speed = 2
      self.stat_hp = 120
    self.xp = 500
    self.stat_faith += dice.lancer(1,10)
    self.stat_strenght += dice.lancer(1,10)
    self.stat_hp += dice.lancer(1,10)
    self.stat_speed += dice.lancer(1,10)
    self.max_hp = self.stat_hp
    Weapon("str",1,0,0)
    Armor(0,0,0)

    print("Vous avez:\n" + str(self.stat_faith) + " point de foi\n" + 
      str(self.stat_strenght) + " point de force\n" + 
      str(self.stat_hp) + " point de vie\n" + 
      str(self.stat_speed) + " de vitesse de deplacement")

    def use_inventory(self):

      choix = int(input("Que voulez vous faire:\n1-Changer d'armure\n2-Changer d'arme\n3-Quitter\n\nReponse: "))
      if choix == 1:
        print("Vous avez:\n" + str(self.inventory_armor))
        choix = int(input("Quelle armure voulez vous prendre?\n\nReponse: "))
        choix -= 1
        if choix < 0:
          choix = 0
        self.use_armor = self.inventory_armor[choix]
        if self.use_armor == "Rien":
          Armor(0,0,0)
          self.armor = Armor(0,0,0)
        elif self.use_armor == "Armure de fer":
          Armor(10,0,5)
          self.armor = Armor(10,0,5)
        elif self.use_armor == "Habit d'inquisiteur":
          Armor(2,10,0)
          self.armor = Armor(2,10,0)
        print("Vous utilisez:\n" + str(self.use_armor)
          + "\nVotre armure a: " +
              str(self.armor.str_protection) + " de protection physique, " + str(self.armor.faith_protection) + " de protection magique et " + str(self.armor.weight) + " de poids")
      elif choix == 2:
        print("Vous avez:\n" + str(self.inventory_weapon))
        choix = int(input("Quelle arme voulez vous prendre?\n\nReponse: "))
        choix -= 1
        if choix < 0:
          choix = 0
        self.use_weapon = self.inventory_weapon[choix]
        if self.use_weapon == "Rien":
          Weapon("str",1,0,0)
          self.weapon = Weapon("str",1,0,0)
        elif self.use_weapon == "Épée":
          Weapon("str",5,0,self.stat_strenght)
          self.weapon = Weapon("str",5,0,self.stat_strenght)
        elif self.use_weapon == "Serment de vérité":
          Weapon("int",0,5,0)
          self.weapon = Weapon("faith",0,5,0)
        print("Vous utilisez:\n" + str(self.use_weapon)
          + "\nVotre arme fais: " + str(self.weapon.damage) + " points de dégâts")

      else:
        print("Ce choix n'est pas disponible")
        use_inventory()
