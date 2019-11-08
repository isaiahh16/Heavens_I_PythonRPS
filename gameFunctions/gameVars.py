from random import randint

choices=["rock", "paper", "scissors"]

#adding lives: when one or the other gets 0, win / lose
player_lives = 1
computer_lives = 1
total_lives = 1

#let the ai make a choice
computer=choices[randint(0, 2)]

#set up a game loop here so we dont have to keep restarting
player = False