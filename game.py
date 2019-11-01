from random import randint

def winorlose(status):
	#print("called win or lose", status "\n")
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N")

	if choice == "Y" or choice == "y":
			global player_lives
			global computer_lives
			global player
			global computer
			#reseth the game
			player_lives = 1
			computer_lives = 1
			player = False
			computer = choices[randint(0, 2)]

	elif choice == "N" or choice == "n":
			print("You chose to quit. Better luck next time.")
			exit()
	else:
			print("Make a valid choice. Yes or No.")


choices=["rock", "paper", "scissors"]

#adding lives: when one or the other gets 0, win / lose
player_lives = 1
computer_lives = 1

#let the ai make a choice
computer=choices[randint(0, 2)]





#set up a game loop here so we dont have to keep restarting
player = False

while player is False:
	print("========================================")
	print("Computer Lives:", computer_lives, "/1\n")
	print("Computer Lives:", player_lives, "/1\n")
	print("========================================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper or scissors: \n")

	# print("computer: ", computer, "player: ", player)

#print(computer, player)
#
#start doing some logic and condition checking
#always check a breking condition first
	if player == computer:
	#we have a tie, no point in going any further
		print("tie, no one wins! try again")
	
	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()
	
	elif player == "rock":
		if computer == "paper":
			print("You Lose!", computer, "covers", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "paper":
		if computer == "scissors":
			print("You Lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Won!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Won!", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1

	if player_lives is 0:
		winorlose("lost")
	# 	print("You lost! Would you like to play again?")
	# 	choice = input("Y / N")

	elif computer_lives is 0:
		winorlose("won")
	# 	print("You won! Would you like to play again?")
	# 	choice = input("Y / N")

	# 	if choice == "Y" or choice == "y":
	# 		#reseth the game
	# 		player_lives = 1
	# 		computer_lives = 1
	# 		player = False
	# 		computer = choices[randint(0, 2)]

	# 	elif choice == "N" or choice == "n":
	# 		print("You chose to quit. Better luck next time.")
	# 		exit()
	# 	else:
	# 		print("Make a valid choice. Yes or No.")

	else:
		player = False
		computer=choices[randint(0,2)]
