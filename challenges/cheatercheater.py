from random import randint

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice):
      if self.dice[i] < 6:
        self.dice[i] += 1
      i += 1

class Lukes_Cheat_Method(Player):
    def cheat(self):
       # i = 0
       # while i < len(self.dice):
           # if self.dice[i] < 6:
               # self.dice[i] += 2
               # if self.dice[i] > 6:
                   # self.dice[i] -= 1
           # elif self.dice[i] < 2:
               # self.dice[i] += 2
            # i += 1
            self.dice = [randint(3, 6) if roll < 6 else roll for roll in self.dice]
