from cheatercheater import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
uppercheater = Lukes_Cheat_Method()
swapper_score = 0
loaded_dice_score = 0
uppercheater_score = 0
number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
  swapper.roll()
  loaded_dice.roll()
  uppercheater.roll()

  swapper.cheat()
  loaded_dice.cheat()
  uppercheater.cheat()
   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) and sum(uppercheater.get_dice()) == sum(swapper.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(uppercheater.get_dice()) < sum(swapper.get_dice()):
 #print("Dice swapper wins!")
   swapper_score+= 1
  elif sum(uppercheater.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) < sum(uppercheater.get_dice()):
      uppercheater_score+= 1
  else:
 #print("Loaded dice wins!")
    loaded_dice_score += 1
  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
print("Luke's cheat method won: " +str(uppercheater_score))
if swapper_score == loaded_dice_score and uppercheater_score:
  print("Game was drawn")
elif swapper_score > loaded_dice_score and uppercheater_score:
  print("Swapper won most games")
elif uppercheater_score > loaded_dice_score and swapper_score:
  print("Luke's cheat method won most games")
else:
  print("Loaded dice won most games")

