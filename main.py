from dice import Dice
from dice import Dice
from player import Player
from fight_manager import FightManager

#initialization des classe

dice = Dice()
player = Player()
dice.lancer(2, 6)
fightManager = FightManager()

def main_menu():
  #aficher le debut de lhistoir
    print("   db    8888Yb Yb  dP .dPY8 .dPY8      db    88         .dP-Y8    db     dP--b8 88--Yb    db    8b    d8 888888 88b 88 888888 ")
    print("  dPYb   88__dP  YbdP   Ybo.   Ybo.    dPYb   88          Ybo.    dPYb   dP      88__dP   dPYb   88b  d88 88__   88Yb88   88   ")
    print(" dP__Yb  88  Yb   8P   o. Y8b o. Y8b  dP__Yb  88  .o     o. Y8b  dP__Yb  Yb      88 Yb   dP__Yb  88YbdP88 88     88 Y88   88   ")
    print("dP    Yb 88oodP  dP    8bodP' 8bodP' dP    Yb 88ood8     8bodP  dP    Yb  YboodP 88  Yb dP    Yb 88 YY 88 888888 88  Y8   88   \n\n\n")
    while True:
      start_game = int(input("1-Commencer   2-Charger\n3-Quitter\n\nReponse: "))
      if start_game == 1:
        break
def level_up():
  choix = int(input("Devant vous ce trouve la statue de l'eveillememt, dieu incontestable\nQue voulez vous faire:\n1-Vous baissez et suppliez votre divinite\n2-Partir\n\nReponse:"))
  if choix == 1:
    print("Vous fermez les yeux et honorez votre serment")
    while player.xp >= 0:
      if player.xp - 100 >= 0:
        choix = int(input("Vous avez " + str(player.xp) + " point de determination\nQue voulez vous faire:\n1-Augmenter votre foi\n2-Augmenter votre force\n3-Augmenter vos point de vie\n4-Vous lever\n\nReponse: "))
        if choix == 1:
          player.stat_faith += 5
          print("Votre lien avec l'illuminé a augmenter, elle est de " + str(player.stat_faith))
          player.xp -= 100
        elif choix == 2:
          player.stat_strenght += 5
          print("Votre forcde a augmenter, elle est de " + str(player.stat_strenght))
          player.xp -= 100
        elif choix == 3:
          player.max_hp += 5
          print("Votre santé maximal a augmenter, elle est de " + str(player.max_hp))
          player.xp -= 100
        elif choix == 4:
          break
      else:
        print("Vous navez pas assez")
        break
stat_player = player.create_player()

print("tu te promene dans la foret et tu vois au loin un ennemi")
fightManager = FightManager(stat_player[0], stat_player[1], stat_player[2], "Épée")
fightManager.printDist()
print("player.hp = " + str(stat_player[0]))
win = fightManager.fight()

if win:
  level_up()

else:
  print("Vous etes mort")
  sys.exit(0)
