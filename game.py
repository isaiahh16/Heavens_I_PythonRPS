from random import randint
from gameFunctions import winlose, gameVars, compare


while gameVars.player is False:
	print("========================================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Computer Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("========================================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper or scissors: \n")

	if  gameVars.player_lives is 0:
		winlose.winorlose("lost")
	# 	print("You lost! Would you like to play again?")
	# 	choice = input("Y / N")

	elif gameVars.computer_lives is 0:
		 winlose.winorlose("won")
	# 	print("You won! Would you like to play again?")
	# 	choice = input("Y / N")

	# 	if choice == "Y" or choice == "y":
	# 		#reseth the game
	# 		player_lives = 1
	# 		gameVars.computer_lives = 1
	# 		player = False
	# 		gameVars.computer = choices[randint(0, 2)]

	# 	elif choice == "N" or choice == "n":
	# 		print("You chose to quit. Better luck next time.")
	# 		exit()
	# 	else:
	# 		print("Make a valid choice. Yes or No.")

	else:
		player = False
		gameVars.computer=gameVars.choices[randint(0,2)]
