from random import randint
from gameFunctions import gameVars

def winorlose(status):
	#print("called win or lose", status "\n")
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N")

	if choice == "Y" or choice == "y":
			#reseth the game
			gameVars.player_lives = 1
			gameVars.computer_lives = 1
			player = False
			gameVars.computer = gameVars.choices[randint(0, 2)]

	elif choice == "N" or choice == "n":
			print("You chose to quit. Better luck next time.")
			exit()
	else:
			print("Make a valid choice. Yes or No.")
			# recursion => calling a function from inside itself
			winorlose(status)