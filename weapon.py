class Weapon:
  def __init__(self,type,str_damage,faith_damage, player_strenght):
    self.str_damage = str_damage
    self.faith_damage = faith_damage 
    self.player_strenght = player_strenght
    self.type = type
    if self.type == "faith":
      self.damage = self.faith_damage
    else:
      self.damage = self.str_damage + self.player_strenght
