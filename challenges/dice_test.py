from cheatercheater import Player
from cheatercheater import Lukes_Cheat_Method
from cheatercheater import Cheat_Loaded_Dice

cheater1 = Cheat_Loaded_Dice()
cheaterLuke = Lukes_Cheat_Method()
cheater1.roll()
cheaterLuke.roll()

cheater1.cheat()
cheaterLuke.cheat()

print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater Luke rolled" + str(cheaterLuke.get_dice()))

if sum(cheater1.get_dice()) == sum(cheaterLuke.get_dice()):
  print("Draw!")

elif sum(cheater1.get_dice()) > sum(cheaterLuke.get_dice()):
  print("Cheater 1 wins!")

else:
  print("Cheater Luke wins!")

