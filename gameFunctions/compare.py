from gameFunctions import gameVars

# figure out what to pass into the function => what are you comparing
#
def compareChoices(player):
	if  player == gameVars.computer:

		print("\033[1;36;40mtie, no one wins! try again.")
	
	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()
	
	elif player == "rock":
		if gameVars.computer == "paper":
			print("\033[1;31;40mYou Lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("\033[1;32;40mYou Won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("1;31;40mYou Lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("\033[1;32;40mYou Won!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "scissors":
		if gameVars.computer == "rock":
			print("1;31;40mYou Lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("\033[1;32;40mYou Won!", player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
