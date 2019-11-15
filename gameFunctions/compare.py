from gameFunctions import gameVars

# figure out what to pass into the function => what are you comparing
#
def compareChoices(player):
	if  player == gameVars.computer:

		print('\033[2J')
		print("\033[1;36;40mTie, no one wins!",("\U0001F610\n"))
	
	elif player == "quit":
		print('\033[2J')
		print("you chose to quit, quitter.",("\U0001F602"))
		exit()
	
	elif player == "rock":
		if gameVars.computer == "paper":
			print('\033[2J')
			print("\033[1;31;40mYou Lose!",("\U0001F614"), gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print('\033[2J')
			print("\033[1;32;40mYou Won!",("\U0001F603"), player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print('\033[2J')
			print("\033[1;31;40mYou Lose!",("\U0001F614"), gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print('\033[2J')
			print("\033[1;32;40mYou Won!",("\U0001F603"), player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "scissors":
		if gameVars.computer == "rock":
			print('\033[2J')
			print("\033[1;31;40mYou Lose!",("\U0001F614"), gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print('\033[2J')
			print("\033[1;32;40mYou Won!",("\U0001F603"), player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
