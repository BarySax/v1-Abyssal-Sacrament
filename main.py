from dice import Dice
from player import Player
from enemy import Enemy

#initialization des classe
enemy = Enemy()

dice = Dice()
player = Player()
dice.lancer(2, 6)

enemy.choose()

dice.lancer(2, 6)