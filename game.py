from random import randint

choices=["rock", "paper", "scissors"]

computer=choices[randint(0,2)]

#set up a game loop here so we dont have to keep restarting
player = False

while player is False:
	player=input("choose rock, paper or scissors: \n")

	print("computer: ", computer, "player: ", player)

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
		else:
			print("You Won!", player, "smashes", computer, "\n")

	elif player == "paper":
		if computer == "scissors":
			print("You Lose!", computer, "cuts", player, "\n")
		else:
			print("You Won!", player, "covers", computer, "\n")

	elif player == "scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
		else:
			print("You Won!", player, "cuts", computer, "\n")


	player = False
	computer=choices[randint(0,2)]
