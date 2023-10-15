class Weapon:
  def __init__(self,type,str_damage,int_damage, player_strenght):
    self.str_damage = str_damage
    self.int_damage = int_damage 
    self.player_strenght = player_strenght
    self.type = type
    if self.type == "int":
      self.damage = self.int_damage
    else:
      self.damage = self.str_damage + self.player_strenght
