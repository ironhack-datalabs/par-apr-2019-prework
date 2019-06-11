# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

import random


# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.

play = [ 'stone', 'paper', 'scissors']

# Assign a variable to the maximum number of games: 1, 3, 5, etc ...

max_games = 6

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games

max_to_win = 2

# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.

machine_player = random.choice(play)
#print(machine_player)
# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.

#human_player = str(input("Enter your choice (stone, paper or scissors): "))
#while human_player != str('stone') and human_player != str('paper') and human_player != str('scissors'):
    #human_player = str(input("Enter your choice (stone, paper or scissors): "))

# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins

'''scissors > paper
paper > stone
stone > scissors'''

# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated
# Create two variables that accumulate the wins of each participant
# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.

nb_of_game = 0
machine_wins = 0
human_wins = 0
tie = 0

while machine_wins <= max_to_win and human_wins <= max_to_win and nb_of_game <= max_games:
    nb_of_game +=1
    machine_player = random.choice(play)
    human_player = str(input("Enter your choice (stone, paper or scissors): "))
    while human_player != str('stone') and human_player != str('paper') and human_player != str('scissors'):
        human_player = str(input("Enter your choice (stone, paper or scissors): "))

    if (machine_player == 'scissors' and human_player == "paper") or (machine_player == "paper" and human_player == "stone") or (machine_player == "stone" and human_player == "scissors"):
        machine_wins +=1
        print("The choice of the player is: ", human_player)
        print("The choice of the machine is: ", machine_player)
        print("The machine wins")

    elif (human_player == 'scissors' and machine_player == "paper") or (human_player == "paper" and machine_player == "stone") or (human_player == "stone" and machine_player == "scissors"):
        human_wins +=1
        print("The choice of the player is: ", human_player)
        print("The choice of the machine is: ", machine_player)
        print("The player wins")

    elif human_player == machine_player:
        tie +=1
        print("The choice of the player is: ", human_player)
        print("The choice of the machine is: ", machine_player)
        print("Tie")

# Print by console the winner of the game based on who has more accumulated wins
if machine_wins < human_wins:
    print("The winner of the game is the human player")
else:
    print("The winner of the game is the machine")

