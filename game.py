from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print("========================================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Computer Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("========================================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper or scissors: \n")
	compare.compareChoices(player)

	if  gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		 winlose.winorlose("won")

	else:
		player = False
		gameVars.computer=gameVars.choices[randint(0,2)]
