from dice import Dice
from dice import Dice
from player import Player
from fight_manager import FightManager

#initialization des classe

dice = Dice()
player = Player()
dice.lancer(2, 6)
fightManager = FightManager()


def level_up():
  if player.p_class == "Chevalier":
    choix = int(input("Devant vous ce trouve la statue de Krilum, prophete de la guerre\nQue voulez vous faire:\n1-Vous baissez et honorez votre serment\n2-Partir\n\nReponse:"))
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
  elif player.p_class == "Inquisiteur":
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

print ("Bienvenue dans le monde de la guerre tu vas choisir ta classe et ton nom")
player.create_player()

print("tu te promene dans la foret et tu vois au loin un ennemi")
fightManager.printDist()
fightManager.tourEnemy()


